import urllib
import urllib2
import json
from twilio.rest import TwilioRestClient
import webapp2
from google.appengine.api import taskqueue
import cgi
import dateutil.parser
import datetime
from APIKeys import account_sid, auth_token, twilio_number

class SetAlarm():
   @staticmethod
   def setalarm(from_number, json_string):
      time = json_string['outcomes'][0]['entities']['datetime'][0]['value']
      alarmTime = dateutil.parser.parse(time)

      taskqueue.add(url="/runalarm", eta=alarmTime, params={'number': from_number})

      return "Alarm set for %d:%d, %d/%d"%(alarmTime.hour,alarmTime.minute,alarmTime.month,alarmTime.day)

class RunAlarm(webapp2.RequestHandler):
   def post(self):
      from_number = cgi.escape(self.request.get('number'))
      client = TwilioRestClient(account_sid, auth_token)
      call = client.calls.create(to="%s"%from_number,from_=twilio_number,url="http://yhack-sms.appspot.com/alarmcall")
      self.response.write("Alarm is running") 
