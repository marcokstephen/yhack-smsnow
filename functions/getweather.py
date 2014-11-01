import urllib
import urllib2

class GetWeather():

   @staticmethod
   def getweather(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)
      weather_url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20%28select%20woeid%20from%20geo.places%281%29%20where%20text%3D%22"+location+"%22%29&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
#      weather_url = "http://api.openweathermap.org/data/2.5/weather?q=%s"%urllib.quote(location)
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()

      return json_result

   @staticmethod
   def getforecast(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)
      weather_url = "https://query.yahooapis.com/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20woeid%20in%20%28select%20woeid%20from%20geo.places%281%29%20where%20text%3D%22"+location+"%22%29&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()

      return json_result
