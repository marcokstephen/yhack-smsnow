import urllib
import urllib2
import json
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

class GetDirection():
   @staticmethod
   def getdirection(json_string):
      origin = json_string['outcomes'][0]['entities']['location'][0]['value']
      destination = json_string['outcomes'][0]['entities']['location'][1]['value']
      origin = urllib.quote(origin)
      destination = urllib.quote(destination)
      maps_url = "https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination

      request = urllib2.Request(maps_url)
      response = urllib2.urlopen(request)
      json_result = response.read()
      json_result_object = json.loads(json_result)
      legs = json_result_object['routes'][0]['legs'][0]

      startAddress = legs['start_address']
      endAddress = legs['end_address']
      distance = legs['distance']['text']

      outputString = "Start: "+startAddress+"\nEnd: "+endAddress+"\nDistance: "+distance+"\n\n"
      header = outputString

      stepsList = legs['steps']
      for x in range(len(stepsList)):
         step = stepsList[x]
         distance = step['distance']['text']
         instructions = step['html_instructions']
         outputString = outputString + "%d: "%(x+1)+instructions+" ("+distance+")\n"

      outputString = GetDirection.strip_tags(outputString)
      if (len(outputString) > 1600):
         outputString = header+"Distance is too great! Try smaller!"
      return outputString

   @staticmethod
   def strip_tags(htmlstring):
      s = MLStripper()
      s.feed(htmlstring)
      return s.get_data()   
