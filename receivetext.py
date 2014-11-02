import webapp2
import cgi
import urllib
import urllib2
from twilio import twiml
import sys
sys.path.append('functions')
from getweather import GetWeather
from getstocks import GetStock
from setalarm import SetAlarm
from getShowInfo import GetShowInfo
from setreminder import SetReminder
from helpme import GetHelp
from gettranslate import GetTranslate
from getdirection import GetDirection
from findnearby import FindNearby
from getPrices import GetProductData

import json

weatherReport = GetWeather()
stockReport = GetStock()
setAlarm = SetAlarm()
setReminder = SetReminder()
showInfo = GetShowInfo()
helpMenu = GetHelp()
translateText = GetTranslate()
getDirection = GetDirection()
findNearby = FindNearby()
getProductData = GetProductData()

class ReceiveText(webapp2.RequestHandler):
   def post(self):
      fromNumber = cgi.escape(self.request.get('From'))
      messageBody = cgi.escape(self.request.get('Body'))

      witUrl = "https://api.wit.ai/message?v=20141031&q=%s"%urllib.quote(messageBody)
      request = urllib2.Request(witUrl)
      request.add_header("Authorization", "Bearer 5OC5HZGDNDB67BXOCNLND44DZP6ZZBRH")
      result = urllib2.urlopen(request)
      json_result = result.read()
      
      json_object_result = json.loads(json_result)
      method_name = json_object_result['outcomes'][0]['intent']
      
      if method_name == "get_weather":
         #get the weather
         json_result = weatherReport.getweather(json_object_result)
      elif method_name == "get_weather_forecast":
         json_result = weatherReport.getforecast(json_object_result)
      elif method_name == "get_stocks":
         json_result = stockReport.getstock(json_object_result)
      elif method_name == "set_alarm":
         json_result = setAlarm.setalarm(fromNumber,json_object_result)
      elif method_name == "get_shows":
         json_result = showInfo.getAllShows(showInfo, json_object_result)
      elif method_name == "get_episodes_today":
         json_result = showInfo.getEpisodesToday(showInfo, json_object_result)
      elif method_name == "set_reminder":
         json_result = setReminder.setreminder(fromNumber,json_object_result)
      elif method_name == "help_me":
         json_result = helpMenu.gethelp()
      elif method_name == "get_translate":
         json_result = translateText.gettranslate(json_object_result)
      elif method_name == "get_directions":
         json_result = getDirection.getdirection(json_object_result)
      elif method_name == "find_nearby":
         json_result = findNearby.findnearby(json_object_result)
      elif method_name == "get_product_info":
         json_result = getProductData.getInfo(getProductData, json_object_result)
      elif method_name == "get_price":
         json_result = getProductData.getPrice(getProductData, json_object_result)
   
      print json_result
      r = twiml.Response()
      try:
         r.message(json_result)
      except:
         r.message(str(json_result))
      self.response.headers['Content-Type'] = 'text/xml'
      self.response.write(str(r))
