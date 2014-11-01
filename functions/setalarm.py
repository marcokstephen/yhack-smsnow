import urllib
import urllib2
import json
from twilio.rest import TwilioRestClient

class SetAlarm():
   @staticmethod
   def setalarm(from_number, json_string):
     
      account_sid = "ACcdd722da9eb23c0be222908001c05621"
      auth_token = "f42dc3d4155e275b7e6534a08d1c12fc"
      client = TwilioRestClient(account_sid, auth_token)
      call = client.calls.create(to=from_number,from_="+12892784272",url="http://104.131.180.180:8080/alarmcall")

      return from_number 
