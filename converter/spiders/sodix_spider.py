import json
import time
import scrapy as scrapy
import converter.env as env

from converter.items import *
from converter.spiders.base_classes.lom_base import LomBase
from scrapy.spiders import CrawlSpider

class SodixSpider(CrawlSpider, LomBase):
    """
    This crawler fetches data from the SODIX. The Scrapy request with GraphQL in JSON (please refer to body in parse() function). 
    The Response will be convert to python dictionary using json.dumps(). Response.meta["item"] is used in every
    get function to facilitate access to metadata. 

    For better understanding, please refer to mediothek_pixiothek_spider.py, merlin_spider.py and openduhub / oeh-search-etl in 
    Github(https://github.com/openeduhub/oeh-search-etl/wiki/How-To-build-a-crawler-for-edu-sharing-(alternative-method))

    Author: BRB team
    """

    name            = "sodix_spider"
    url             = "https://www.sodix.de/"  # the url which will be linked as the primary link to your source (should be the main url of your site)
    friendlyName    = "Sodix"  # name as shown in the search ui
    version         = "0.1"  # the version of your crawler, used to identify if a reimport is necessary
    apiUrl          = "https://api.sodix.de/gql/auth/login"  # * regular expression, to represent all possible values.
    apiUrl2         = "https://api.sodix.de/gql/graphql"
    user            = env.get("SODIX_USER")
    password        = env.get("SODIX_PASSWORD")

    def __init__(self, **kwargs):
        LomBase.__init__(self, **kwargs)

    # login into sodix page, then call parse function. 
    def start_requests(self):    
        yield scrapy.Request(
            url      = self.apiUrl,
            callback = self.parse,
            method   = 'POST',
            headers  = { 'Content-Type': 'application/json' },
            body     ="{\"login\": \""+self.user+"\",\"password\": \""+self.password+"\"}"
        )
                 
    def parse(self, response: scrapy.http.Response):
        json_response_body  = json.loads(response.body) if response.status==200 else print("LOGIN ERROR")
        
        access_token        = str(json_response_body['access_token'])
        headers             = { 
                                'Authorization':'Bearer ' + access_token,
                                'Content-Type' : 'application/json'
                              } 

        # add the metadata that you want to extract here
        body         = json.dumps({"query":
                                        "{\n sources { id\n name\n created\n metadata { description\n keywords\n language\n learnResourceType\n media { dataType\n originalUrl\n size\n thumbPreview\n } publishers { linkToGeneralUseRights\n } title\n } }\n}"})
        yield scrapy.Request(
                                url      = self.apiUrl2,
                                callback = self.parse_sodix,
                                method   = 'POST',
                                headers  = headers,
                                body     = body   
                            ) 

    # to access sodix with access_token
    def parse_sodix(self, response):
        elements     = json.loads(response.body.decode('utf-8'))
        requestCount = len(elements['data']['sources'])

        for i in range(requestCount):
        # For debugging
            # if i == 10:
            #     print('dev-mode : 10 requests done, exiting...')
            #     break

            copyResponse              = response.copy()
            copyResponse.meta["item"] = elements['data']['sources'][i] 

            json_str = json.dumps(elements['data']['sources'][i], indent=4, sort_keys=True, ensure_ascii=False)

            copyResponse._set_body(json_str)

            # In order to transfer data to CSV/JSON, implement these 2 lines. 
            if self.hasChanged(copyResponse):
               yield LomBase.parse(self, copyResponse)
            
            # to call LomBase functions 
            LomBase.parse(self, copyResponse)
            print('Finish parsing: ' + str(i+1) + '/' + str(requestCount))
    
    def getBase(self, response):
        base         = LomBase.getBase(self, response)
        source       = response.meta["item"]

        for i in range(len(source['metadata'])):
            base.add_value("thumbnail"  , source['metadata'][i]['media']['thumbPreview'])        
        return base  

    def getId(self, response) :
        source = response.meta["item"]
        return source['id']

    def getHash(self, response):
        return hash(str(self.version)+str(time.time()))

    def mapResponse(self, response):
        r = ResponseItemLoader(response=response)
        r.add_value("status"    , response.status)
        r.add_value("headers"   , response.headers)
        r.add_value("url"       , response.url)
        return r     

    def getLOMEducational(self, response=None):
        educational = LomBase.getLOMEducational(self, response)
        source      = response.meta["item"]

        for i in range(len(source['metadata'])):
            educational.add_value("description" , source['metadata'][i]['description'])
            educational.add_value("language"    , source['metadata'][i]['language'])
        return educational
    
    def getLOMGeneral(self, response):
        general = LomBase.getLOMGeneral(self, response)
        source  = response.meta["item"]

        general.add_value("identifier"  , source['id'])

        for i in range(len(source['metadata'])):
            general.add_value("title"       , source['metadata'][i]['title'])        
            general.add_value("keyword"     , source['metadata'][i]['keywords'])
            general.add_value("language"    , source['metadata'][i]['language'])
            general.add_value("description" , source['metadata'][i]['description'])
            return general
    
    def getLicense(self, response=None):
        license = LomBase.getLicense(self, response)
        source  = response.meta["item"]
 
        for i in range(len(source['metadata'])):
            for j in range(len(source['metadata'][i]['publishers'])):
                license.add_value("description",source['metadata'][i]['publishers'][j]['linkToGeneralUseRights'])
        return license

    def getLOMTechnical(self, response):
        technical = LomBase.getLOMTechnical(self, response)
        source    = response.meta["item"]

        for i in range(len(source['metadata'])):
            technical.add_value("format"    , source['metadata'][i]['media']['dataType'])
            technical.add_value("location"  , source['metadata'][i]['media']['originalUrl'])
            technical.add_value("size"      , source['metadata'][i]['media']['size'])
        return technical

    def getValuespaces(self, response):
        valuespaces = LomBase.getValuespaces(self, response)
        source      = response.meta["item"]

        for i in range(len(source['metadata'])):
            valuespaces.add_value("learningResourceType", source['metadata'][i]['learnResourceType'])

        return valuespaces
    
    # TODO
    def getPermissions(self, response):
        permissions = LomBase.getPermissions(self, response)
        return permissions    

    # TODO 
    def getLOMAnnotation(self, response=None) -> LomAnnotationItemLoader:
        annotation = LomBase.getLOMAnnotation(self, response)
        return annotation

    # TODO
    def getLOMRelation(self, response=None) -> LomRelationItemLoader:
        relation = LomBase.getLOMRelation(self, response)
        return relation