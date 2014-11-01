import json
import webapp2
from google.appengine.api import taskqueue
import cgi
from twilio.rest import TwilioRestClient

class SetReminder():
   @staticmethod
   def setreminder(number,json_string):
      reminder = json_string['outcomes'][0]['entities']['reminder'][0]['value']

      #7200 seconds = 2 hours for a reminder countdown
      taskqueue.add(url="/runreminder", countdown=7200, params={'number':number,'reminder':reminder})

      return "Reminder set: "+reminder

class RunReminder(webapp2.RequestHandler):
   def post(self):
      number = cgi.escape(self.request.get('number')
      reminder = cgi.escape(self.request.get('reminder')
      account_sid = "ACcdd722da9eb23c0be222908001c05621"
      auth_token = "f42dc3d4155e275b7e6534a08d1c12fc"
      client = TwilioRestClient(account_sid, auth_token)
      rv = client.messages.create(to="%s"%number, from_="+12892784272",body=reminder)
      self.response.write("Reminder is being sent.")
