import urllib
import urllib2

class GetWeather():
   def getweather(location):
      weather_url = "http://api.openweathermap.org/data/2.5/weather?q=%s"%urllib.quote(location)
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()

      return json_result
