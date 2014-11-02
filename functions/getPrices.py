import urllib
import urllib2
import json
import datetime

class GetProductData():

   #@staticmethod
   #def getInfo(self, json_string):

   @staticmethod
   def getPurchaseLocation(self, json_string):
      json_query_result = self.curlRequest(self, json_string)
      item_list = json_query_result['results']

      maxlist = min(len(item_list), 5)
      item_names_list = []
      item_productinfo_list = []
      
      for x in range (0, maxlist):
         item_tripletinfo = []
         try:
            item_names_list.append(item_list[x]['name'])
            item_tripletinfo.append(item_list[x]['sitedetails'][0]['latestoffers'][0]['seller'])
            item_tripletinfo.append(item_list[x]['sitedetails'][0]['latestoffers'][0]['price'])
            item_tripletinfo.append(item_list[x]['sitedetails'][0]['latestoffers'][0]['availability'])
         except:
            continue
         item_productinfo_list.append(item_tripletinfo)

      json_product_info = dict(zip(item_names_list, item_productinfo_list))
      return str(json_product_info)


   @staticmethod
   def getPrice(self, json_string):
      json_query_result = self.curlRequest(self, json_string)
      item_list = json_query_result['results']
      #Maximum listings is 5
      maxlist = min(len(item_list), 5)
      item_names_list = []
      item_price_list = []
      for x in range (0, maxlist):
         try: 
            item_names_list.append(item_list[x]['name'])
            item_price_list.append(item_list[x]['price'])
         except:
            continue

      json_nameprice = dict(zip(item_names_list, item_price_list))
      return str(json_nameprice)


   @staticmethod
   def curlRequest(self, json_string):
      searchQuery = self.getSearchQuery(self, json_string)
      sem_url= "https://api.semantics3.com/test/v1/products?q={\"search\":\"%s\"}" %urllib.quote(searchQuery)
      request = urllib2.Request(sem_url)
      request.add_header("api_key", "SEM369667FA6AFAB6FBE6D2DF989D51141F6")
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_result_object = json.loads(json_result)
      return json_result_object

   @staticmethod
   def getSearchQuery(self, json_string):
      return json_string['outcomes'][0]['entities']['search_query'][0]['value']

   