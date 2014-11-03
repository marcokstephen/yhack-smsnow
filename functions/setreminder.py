import json
import webapp2
from google.appengine.api import taskqueue
import cgi
from twilio.rest import TwilioRestClient
from APIKeys import account_sid, auth_token, twilio_number

class SetReminder():
   @staticmethod
   def setreminder(number,json_string):
      reminder = json_string['outcomes'][0]['entities']['reminder'][0]['value']

      #7200 seconds = 2 hours for a reminder countdown
      taskqueue.add(url="/runreminder", countdown=7200, params={'number':number,'reminder':reminder})

      return "Reminder set: "+reminder

class RunReminder(webapp2.RequestHandler):
   def post(self):
      number = cgi.escape(self.request.get('number'))
      reminder = cgi.escape(self.request.get('reminder'))
      client = TwilioRestClient(account_sid, auth_token)
      rv = client.messages.create(to="%s"%number, from_=twilio_number,body=reminder)
      self.response.write("Reminder is being sent.")
