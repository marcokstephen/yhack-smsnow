import urllib
import urllib2
import json

class GetWeather():

   @staticmethod
   def getweather(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)
      weather_url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20%28select%20woeid%20from%20geo.places%281%29%20where%20text%3D%22"+location+"%22%29&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)

      temperature = json_object_result['query']['results']['channel']['item']['condition']['temp']
      condition = json_object_result['query']['results']['channel']['item']['condition']['text']
      date = json_object_result['query']['results']['channel']['item']['condition']['date']
      output_string = condition+"\n"+temperature+" degrees\n"+date

      return output_string

   @staticmethod
   def getforecast(json_string):
      location = json_string['outcomes'][0]['entities']['location'][0]['value']
      location = urllib.quote(location)
      weather_url = "https://query.yahooapis.com/v1/public/yql?q=select%20item%20from%20weather.forecast%20where%20woeid%20in%20%28select%20woeid%20from%20geo.places%281%29%20where%20text%3D%22"+location+"%22%29&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
      request = urllib2.Request(weather_url)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)

      forecast_list = json_object_result['query']['results']['channel']['item']['forecast']

      output_string = ""
      for forecast_day in forecast_list:
         date = forecast_day['date']
         high = forecast_day['high']
         low = forecast_day['low']
         condition = forecast_day['text']
         daily_string = date+"\nHigh: "+high+"\nLow: "+low+"\n"+condition+"\n\n"
         output_string = output_string + daily_string

      return output_string
