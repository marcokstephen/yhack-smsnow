import urllib
import urllib2

class GetWeather():

   @staticmethod
   def getweather(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      weather_url = "http://api.openweathermap.org/data/2.5/weather?q=%s"%urllib.quote(location)
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()

      return json_result
