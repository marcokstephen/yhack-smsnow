import urllib
import urllib2
import json

class GetShowInfo():

   @staticmethod
   def getShowsToday(json_string):
      contentType = "shows"
      aspect = ""
      show_url = "http://api.viacom.com/v12/%s%s?apiKey=vT4Aq18ANEmQFPZI4jxFpJFypuGrwmVK " % (contentType, aspect)
      request = urllib2.Request(show_url)
      result = urllib2.urlopen(request)
      json_result = result.read()

      json_result_object = json.loads(json_result)

      json_shows = ""
      test_result = json_result_object['response']['Shows']
      for x in range (0, len(test_result)):
         json_shows += test_result[x]['Title']
         json_shows += ", "

      return json_shows
