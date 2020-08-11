import json
import time
from datetime import datetime

from scrapy.spiders import CrawlSpider
from converter.items import *
from converter.offline_mode.mediothek_pixiothek_spider_offline import encode_url_for_local
from converter.spiders.lom_base import LomBase
from converter.constants import *;


class MediothekPixiothekSpider(CrawlSpider, LomBase):
    """
    This crawler fetches data from the Mediothek/Pixiothek. The API request sends all results in one page. The outcome is an JSON array which will be parsed to their elements.

    Author: Timur Yure, timur.yure@capgemini.com , Capgemini for Schul-Cloud, Content team.
    """
    name = 'mediothek_pixiothek_spider'
    url = 'https://www.schulportal-thueringen.de/'  # the url which will be linked as the primary link to your source (should be the main url of your site)
    friendlyName = 'MediothekPixiothek'  # name as shown in the search ui
    version = '0.1'  # the version of your crawler, used to identify if a reimport is necessary
    # start_urls = ['https://www.schulportal-thueringen.de/tip-ms/api/public_mediothek_metadatenexport/publicMediendatei']
    start_urls = ['http://localhost:8080/tip-ms/api/public_mediothek_metadatenexport/publicMediendatei']

    def __init__(self, **kwargs):
        LomBase.__init__(self, **kwargs)

    def parse(self, response: scrapy.http.Response):

        # Call Splash only once per page (that contains multiple XML elements).
        data = self.getUrlData(response.url)
        response.meta["rendered_data"] = data
        elements = json.loads(response.body_as_unicode())

        grouped_elements = self.group_elements(elements)

        for i, element in enumerate(grouped_elements):
            copyResponse = response.copy()

            # Passing the dictionary for easier access to attributes.
            copyResponse.meta['item'] = element

            # In case JSON string representation is preferred:
            json_str = json.dumps(element, indent=4, sort_keys=True, ensure_ascii=False)
            copyResponse._set_body(json_str)
            print(json_str)

            if self.hasChanged(copyResponse):
                yield self.handleEntry(copyResponse)

            # LomBase.parse() has to be called for every individual instance that needs to be saved to the database.
            LomBase.parse(self, copyResponse)

    def group_elements(self, elements):
        """
        This method groups the corresponding elements based on their mediumId. This changes the logic so that every
        element in the end maps to an educational element in the https://www.schulportal-thueringen.de.
        """

        medium_id_groups = {}
        for idx, element in enumerate(elements):
            medium_id = element["mediumId"]

            # The first element that has this mediumId creates the representative for this medium.
            if medium_id not in medium_id_groups:
                medium_id_groups[medium_id] = {
                    "id": medium_id,
                    "pts": self.get_or_default(element, "pts"),
                    "previewImageUrl": self.get_or_default(element, "previewImageUrl"),
                    "titel": self.get_or_default(element, "einzeltitel"),
                    "kurzinhalt": self.get_or_default(element, "kurzinhalt"),
                    "listeStichwort": self.get_or_default(element, "listeStichwort"),
                    "oeffentlich": self.get_or_default(element, "oeffentlich"),
                    "downloadUrl": "https://www.schulportal-thueringen.de/web/guest/media/detail?tspi=" + str(medium_id)
                }

            # TODO: Discuss when it makes sense to combine "serientitel" and "einzeltitel"!
            # The first element to have a serientitel for this mediumId will save it. The rest will just skip it.
            if "serientitel" in element and "serientitel" not in medium_id_groups[medium_id]:
                medium_id_groups[medium_id]["titel"] = element["serientitel"]
                medium_id_groups[medium_id]["serientitel"] = element["serientitel"]
                if "einzeltitel" in element:
                    medium_id_groups[medium_id]["titel"] += " - " + element["einzeltitel"]
                    medium_id_groups[medium_id]["einzeltitel"] = element["einzeltitel"]


        grouped_elements = [medium_id_groups[medium_id] for medium_id in medium_id_groups]

        return grouped_elements

    def get_or_default(self, element, attribute, default_value=""):
        if attribute in element:
            return element[attribute]
        else:
            return default_value

    def getId(self, response):
        # Element response as a Python dict.
        element_dict = response.meta["item"]

        return element_dict["id"]

    def getHash(self, response):
        # Element response as a Python dict.
        element_dict = response.meta["item"]
        # presentation timestamp (PTS)
        id = element_dict["id"]
        pts = element_dict["pts"]
        # date_object = datetime.strptime(hash, "%Y-%m-%d %H:%M:%S.%f").date()
        return id + pts

    def mapResponse(self, response):
        r = ResponseItemLoader(response = response)
        r.add_value('status',response.status)
        r.add_value('headers',response.headers)
        r.add_value('url', self.getUri(response))
        return r

    def handleEntry(self, response):
        return LomBase.parse(self, response)

    def getBase(self, response):
        base = LomBase.getBase(self, response)

        # Element response as a Python dict.
        element_dict = response.meta["item"]

        # TODO: "For licensing reasons, this content is only available to users registered in the Thuringian school
        #  portal."
        # base.add_value('thumbnail', element_dict['previewImageUrl'])

        # TODO: Remove this. This is only for a local execution of Mediothek to check whether Edu-Sharing has issues.
        thumbnail = element_dict['previewImageUrl']
        thumbnail = thumbnail.replace("https://www.schulportal-thueringen.de/", "http://localhost:8080/thumbnails/")
        # Fix the encoding
        thumbnail = encode_url_for_local(thumbnail)
        base.add_value('thumbnail', thumbnail)

        return base

    def getLOMGeneral(self, response):
        general = LomBase.getLOMGeneral(self, response)

        # Element response as a Python dict.
        element_dict = response.meta["item"]

        # TODO: Decide which title. Do we have to construct the title, by concatenating multiple from the provided ones?
        # Einzeltitel, einzeluntertitel, serientitel, serienuntertitel
        general.add_value('title', element_dict["titel"])
        # self._if_exists_add(general, element_dict, "description", "kurzinhalt")
        if "kurzinhalt" in element_dict:
            general.add_value('description', element_dict["kurzinhalt"])

        liste_stichwort = element_dict["listeStichwort"] if "listeStichwort" in element_dict else None
        if liste_stichwort is not None and len(liste_stichwort) > 0:
            general.add_value('keyword', liste_stichwort)

        return general

    def getUri(self, response):
        # Element response as a Python dict.
        element_dict = response.meta["item"]

        return element_dict['downloadUrl']

    def getLicense(self, response):
        license = LomBase.getLicense(self, response)

        # Element response as a Python dict.
        element_dict = response.meta["item"]

        if "oeffentlich" in element_dict and element_dict["oeffentlich"] == "0":  # private
            license.replace_value('internal', Constants.LICENSE_NONPUBLIC)
        else:
            license.replace_value('internal', Constants.LICENSE_COPYRIGHT_LAW)  # public

        return license

    def getLOMTechnical(self, response):
        technical = LomBase.getLOMTechnical(self, response)

        technical.add_value('format', 'text/html')
        technical.add_value('location', self.getUri(response))
        technical.add_value('size', len(response.body))

        return technical


    def getPermissions(self, response):
        """
        Licensing information is controlled via the 'oeffentlich' flag. When it is '1' it is available to the public,
        otherwise only to Thuringia. Therefore, when the latter happens we set the public to private, and set the groups
        and mediacenters accordingly.
        """
        permissions = LomBase.getPermissions(self, response)

        # Self-explained. Only 1 media center in this case.
        permissions.add_value("autoCreateGroups", True)
        # permissions.add_value("autoCreateMediacenters", True)

        element_dict = response.meta["item"]
        permissions.replace_value('public', False)
        if "oeffentlich" in element_dict and element_dict["oeffentlich"] == "0":  # private
            permissions.add_value('groups', ['Thuringia-private'])
            # permissions.add_value('mediacenters', [self.name])  # only 1 mediacenter.
        else:
            permissions.add_value('groups', ['Thuringia-public'])

        return permissions