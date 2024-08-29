import datetime
import json
import logging
import requests
import scrapy
import sys
import vobject

from converter.es_connector import EduSharingConstants
from converter.items import LomAgeRangeItemLoader
from converter.spiders.base_classes.lom_base import LomBase

class TestSpider(LomBase, scrapy.Spider):
    name = "test_spider"
    allowed_domains = ["redaktion.openeduhub.net"]

    API_URL = 'https://redaktion.openeduhub.net/edu-sharing/'
    MDS_ID = 'mds_oeh'

    total = -1
    offset = 0
    count = 100

    def __init__(self, **kwargs):
        LomBase.__init__(self, **kwargs)

        self.log = logging.getLogger('OehImporter')
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(logging.FileHandler('oeh2_output.txt'))

        self.fake_request = scrapy.http.Request(self.API_URL)
        self.fake_response = scrapy.http.Response(self.API_URL, request=self.fake_request)

    def start_requests(self):
        url = f'https://redaktion.openeduhub.net/edu-sharing/rest/search/v1/queries/-home-/{self.MDS_ID}/ngsearch?contentType=FILES&maxItems={self.count}&skipCount={self.offset}&sortProperties=cm%3Acreated&sortAscending=true&propertyFilter=-all-'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        body = {
            'criteria': []
        }
        yield scrapy.Request(url=url, body=json.dumps(body), headers=headers, method='POST', callback=self.parse)
    
    async def parse(self, response):
        data = json.loads(response.body)

        if self.total == -1:
            self.total = data['pagination']['total']
        
        nodes = data['nodes']
        for j in range(len(nodes)):
            node = nodes[j]
            self.log.debug(f'{datetime.datetime.now()} {self.offset+j} / {self.total} :: {node["ccm:replicationsource"] if "ccm:replicationsource" in node else ""} :: {node["name"]}')
            ending = node['name'].rsplit('.', 1)[-1]
            if ending in ('mp4', 'h5p'):
                self.log.info('skipped')
                continue
            
            response_copy = self.fake_response.replace(url=node['content']['url'])
            self.fake_response.meta['item'] = node

            item = await LomBase.parse(self, response_copy)
            yield item

        self.offset += len(nodes)
        if self.offset < self.total:
            url = f'https://redaktion.openeduhub.net/edu-sharing/rest/search/v1/queries/-home-/{self.MDS_ID}/ngsearch?contentType=FILES&maxItems={self.count}&skipCount={self.offset}&sortProperties=cm%3Acreated&sortAscending=true&propertyFilter=-all-'
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
            body = {
                'criteria': []
            }
            yield scrapy.Request(url=url, body=json.dumps(body), headers=headers, method='POST', callback=self.parse)

    def getProperty(self, name, response):
        return (
            response.meta["item"]["properties"][name]
            if name in response.meta["item"]["properties"]
            else None
        )

    def getBase(self, response):
        base = LomBase.getBase(self, response)
        base.replace_value("thumbnail", response.meta["item"]["preview"]["url"])
        base.replace_value(
            "origin", self.getProperty("ccm:replicationsource", response)
        )
        if self.getProperty("ccm:replicationsource", response):
            # imported objects usually have the content as binary text
            # TODO: Sometimes, edu-sharing redirects if no local content is found, and this should be html-parsed
            if response.meta["item"]["downloadUrl"]:
                try:
                    r = requests.get(response.meta["item"]["downloadUrl"])
                    if r.status_code == 200:
                        base.replace_value("fulltext", r.text)
                except:
                    logging.warning(
                        "error fetching data from " + str(response.meta["item"]["downloadUrl"]),
                        sys.exc_info()[0],
                    )
        # TODO
        #else:
        #    # try to transform using alfresco
        #    r = requests.get(
        #        self.apiUrl
        #        + "/node/v1/nodes/"
        #        + response.meta["item"]["ref"]["repo"]
        #        + "/"
        #        + response.meta["item"]["ref"]["id"]
        #        + "/textContent",
        #        headers={"Accept": "application/json"},
        #    ).json()
        #    if "text" in r:
        #        base.replace_value("fulltext", r["text"])

        return base

    # fulltext is handled in base, response is not necessary
    async def mapResponse(self, response, fetchData=True):
        return await LomBase.mapResponse(self, response, False)

    def getId(self, response=None) -> str:
        return response.meta["item"]["ref"]["id"]

    def getHash(self, response=None) -> str:
        return self.version + response.meta["item"]["properties"]["cm:modified"][0]

    def getLOMGeneral(self, response):
        general = LomBase.getLOMGeneral(self, response)
        general.replace_value("title", response.meta["item"]["title"])
        general.add_value(
            "keyword", self.getProperty("cclom:general_keyword", response)
        )
        general.add_value(
            "description", self.getProperty("cclom:general_description", response)
        )
        general.replace_value("aggregationLevel", "1")
        return general

    def getLOMEducational(self, response):
        educational = LomBase.getLOMEducational(self, response)
        tar_from = self.getProperty("ccm:educationaltypicalagerange_from", response)
        tar_to = self.getProperty("ccm:educationaltypicalagerange_to", response)
        if tar_from and tar_to:
            range = LomAgeRangeItemLoader()
            range.add_value("fromRange", tar_from)
            range.add_value("toRange", tar_to)
            educational.add_value("typicalAgeRange", range.load_item())
        return educational

    def getLOMLifecycle(self, response):
        lifecycle = LomBase.getLOMLifecycle(self, response)
        for role in EduSharingConstants.LIFECYCLE_ROLES_MAPPING.keys():
            entry = self.getProperty("ccm:lifecyclecontributer_" + role, response)
            if entry and entry[0]:
                # TODO: we currently only support one author per role
                vcard = vobject.readOne(entry[0])
                if hasattr(vcard, "n"):
                    given = vcard.n.value.given
                    family = vcard.n.value.family
                    lifecycle.add_value("role", role)
                    lifecycle.add_value("firstName", given)
                    lifecycle.add_value("lastName", family)
        return lifecycle

    def getLOMTechnical(self, response):
        technical = LomBase.getLOMTechnical(self, response)
        technical.replace_value("format", "text/html")
        technical.replace_value("duration", self.getProperty("cclom:duration", response))
        if 'ccm:wwwurl' in response.meta['item']['properties']:
            technical.replace_value("location", response.meta["item"]["properties"]["ccm:wwwurl"][0])
        else:
            technical.replace_value("location", response.url)
        return technical

    def getLicense(self, response):
        license = LomBase.getLicense(self, response)
        license.add_value("url", response.meta["item"]["license"]["url"])
        license.add_value(
            "internal", self.getProperty("ccm:commonlicense_key", response)
        )
        license.add_value("author", self.getProperty("ccm:author_freetext", response))
        return license

    def getValuespaces(self, response):
        valuespaces = LomBase.getValuespaces(self, response)
        valuespaces.add_value("discipline", self.getProperty("ccm:taxonid", response))
        valuespaces.add_value(
            "intendedEndUserRole",
            self.getProperty("ccm:educationalintendedenduserrole", response),
        )
        valuespaces.add_value(
            "educationalContext", self.getProperty("ccm:educationalcontext", response)
        )
        valuespaces.add_value(
            "learningResourceType",
            self.getProperty("ccm:educationallearningresourcetype", response),
        )
        valuespaces.add_value(
            "sourceContentType", self.getProperty("ccm:sourceContentType", response)
        )
        valuespaces.add_value(
            "toolCategory", self.getProperty("ccm:toolCategory", response)
        )
        return valuespaces

    def getPermissions(self, response):
        permissions = LomBase.getPermissions(self, response)
        permissions.replace_value("public", False)
        return permissions

    def shouldImport(self, response=None):
        return "ccm:collection_io_reference" not in response.meta["item"]["aspects"]