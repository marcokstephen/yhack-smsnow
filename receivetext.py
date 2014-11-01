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
import json

weatherReport = GetWeather()
stockReport = GetStock()
setAlarm = SetAlarm()
setReminder = SetReminder()
showInfo = GetShowInfo()
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
         json_result = showInfo.getShowsToday(json_object_result)
      elif method_name == "set_reminder":
         json_result = setReminder.setreminder(fromNumber,json_object_result)
#      else:
#         #do nothing


      r = twiml.Response()
      r.message(json_result)
      self.response.headers['Content-Type'] = 'text/xml'
      self.response.write(str(r))
