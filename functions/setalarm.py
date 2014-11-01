import urllib
import urllib2
import json
from twilio.rest import TwilioRestClient
import webapp2
from google.appengine.api import taskqueue
import cgi

class SetAlarm():
   @staticmethod
   def setalarm(from_number, json_string):
      time = json_string['outcomes'][0]['entities']['datetime'][0]['value']

      taskqueue.add(url="/runalarm", countdown=30, params={'number': from_number})

      return from_number

class RunAlarm(webapp2.RequestHandler):
   def post(self):
      from_number = cgi.escape(self.request.get('number'))
      account_sid = "ACcdd722da9eb23c0be222908001c05621"
      auth_token = "f42dc3d4155e275b7e6534a08d1c12fc"
      client = TwilioRestClient(account_sid, auth_token)
      call = client.calls.create(to="%s"%from_number,from_="+12892784272",url="http://104.131.180.180:8080/alarmcall")
      self.response.write("Alarm is running") 
