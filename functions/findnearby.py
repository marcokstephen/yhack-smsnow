import urllib
import urllib2
import json

class FindNearby():
   @staticmethod
   def findnearby(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)
      key = "AIzaSyCH7BZIQ7JP-m02hvzPVa9a8wVGfamAvEI"
      
      #Finding the latitude and longitude with geocode api
      geocode_api = "http://maps.googleapis.com/maps/api/geocode/json?address="+location
      request = urllib2.Request(geocode_api)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)
      
      fullAddressName = json_object_result['results'][0]['formatted_address']
      lat = json_object_result['results'][0]['geometry']['location']['lat']
      lng = json_object_result['results'][0]['geometry']['location']['lng']
      str_lat = str(lat)
      str_lng = str(lng)

      #using the lat and lng with the places api to find nearby attractions
      places_api = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location="+str_lat+","+str_lng+"&radius=3000&types=movie_theater|restaurant|shopping_mall&key="+key
      request = urllib2.Request(places_api)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)
      
      resultsList = json_object_result['results']
      idList = []
      for x in range(0,min(5,len(resultsList))):
         result = resultsList[x]
         place_id = result['place_id']
         idList.append(place_id)

      #using the places api to find more detailed information on the place 
      outputString = ""
      for x in range(0,len(idList)):
        details_api = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+idList[x]+"&key="+key
        place_request = urllib2.Request(details_api)
        place_result = urllib2.urlopen(place_request)
        place_json = place_result.read()
        place_json_object = json.loads(place_json)
        name = place_json_object['result']['name']
        address = place_json_object['result']['formatted_address']
        outputString = outputString + name+"\n"+address+"\n\n"

      return outputString
