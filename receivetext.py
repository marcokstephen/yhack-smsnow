import webapp2
import cgi
import urllib
import urllib2
from twilio import twiml
import sys
sys.path.append('functions')
from getweather import GetWeather
import json

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
      

#      json_result = json_object_result['outcomes']
      self.response.write(json_object_result['outcomes'][0]['intent'])
#      r = twiml.Response()
#      r.message(json_result)
#      self.response.headers['Content-Type'] = 'text/xml'
#      self.response.write(str(r))
