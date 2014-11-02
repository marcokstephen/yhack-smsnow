import urllib
import urllib2
import json
import datetime

class FindHotel():
   @staticmethod
   def findhotel(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)

      #Finding the latitude and longitude with geocode api
      geocode_api = "http://maps.googleapis.com/maps/api/geocode/json?address="+location
      request = urllib2.Request(geocode_api)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)

      lat = json_object_result['results'][0]['geometry']['location']['lat']
      lng = json_object_result['results'][0]['geometry']['location']['lng']
      str_lat = str(lat)
      str_lng = str(lng)

      today = datetime.datetime.now()
      current_date_string = str(today.year)+str(today.month).zfill(2)+str(today.day).zfill(2)
      today += datetime.timedelta(days=1)
      tomorrow_date_string = str(today.year)+str(today.month).zfill(2)+str(today.day).zfill(2)
      
      priceline_url = "http://www.priceline.com/api/hotelretail/listing/v3/"+str_lat+","+str_lng+"/"+current_date_string+"/"+tomorrow_date_string+"/1/15"

      request = urllib2.Request(priceline_url)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)
      
      hmiSortedList = json_object_result['hmiSorted']
      hmiHotels = []
      for x in range(0,min(5,len(hmiSortedList))):
         hmiHotels.append(json_object_result['hotels'][str(hmiSortedList[x])])
      
      outputString = ""
      for hotel in hmiHotels:
         price = hotel['merchPrice']
         currency = hotel['currencyCode']
         starRating = str(hotel['starRating'])
         name = hotel['hotelName']
         addressLn1 = hotel['address']['addressLine1']
         city = hotel['address']['cityName']
         if int(price) < 100:
            outputString += name + "\n"+addressLn1+"\n"+city+"\n"+starRating+" stars\n$"+str(price)[:5]+" "+currency+"\n\n"
         else:
            outputString += name + "\n"+addressLn1+"\n"+city+"\n"+starRating+" stars\n$"+str(price)[:6]+" "+currency+"\n\n"

      return outputString
