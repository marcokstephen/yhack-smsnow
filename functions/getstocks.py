import urllib
import urllib2
import json

class GetStock():
   @staticmethod
   def getstock(json_string):
      company = json_string['outcomes'][0]['entities']['search_query'][0]['value']
      company = urllib.quote(company)

      stock_url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22"+company+"%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
      request = urllib2.Request(stock_url)
      result = urllib2.urlopen(request)
      json_result = result.read()
      json_object_result = json.loads(json_result)

      name = json_object_result['query']['results']['quote']['Name']
      symbol = json_object_result['query']['results']['quote']['Symbol']
      change = json_object_result['query']['results']['quote']['Change']
      lastTrade = json_object_result['query']['results']['quote']['LastTradePriceOnly']
      daysLow = json_object_result['query']['results']['quote']['DaysLow']
      daysHigh = json_object_result['query']['results']['quote']['DaysHigh']

      output_string = name +" ("+symbol+")\nChange: "+change+"\nLast trade: "+lastTrade+"\nDay Low: "+daysLow+"\nDay High: "+daysHigh

      return output_string
