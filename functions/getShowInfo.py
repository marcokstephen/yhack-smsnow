import urllib
import urllib2
import json
import datetime

class GetShowInfo():

   @staticmethod
   def getAllShows(self, json_string): #This is currently too big for text messages
      
      show_url = self.makeGetRequest("shows", "")
      json_result = self.getJsonResult(show_url)
      json_result_object = json.loads(json_result)

      #Initialize the array in which all show titles willgo
      json_shows = ""

      test_result = json_result_object['response']['Shows']
      for x in range (0, len(test_result)-1):
         json_shows += test_result[x]['Title']
         json_shows += ", "

      return json_shows

   @staticmethod
   def getEpisodesToday(self, json_string):
      #Find the time for the request
      date = (self.getDate(json_string))[:10]
     # print date
      show_codes = self.getShowCodes(self)
      #print "CODES: "
      #print show_codes
      episodesList = []
     # print len(show_codes)
      for x in range(0, 30):#len(show_codes) - 1): #We don't iterate through everything for demonstration purposes
         #print show_codes[x]
         episode_byshow_url = self.makeGetRequest("shows/"+show_codes[x], "/episodes")
         #print "EPISODE BY SHOW URL" + episode_byshow_url
         json_episodes = self.getJsonResult(episode_byshow_url)
         #print json_episodes
         json_episodes_object = json.loads(json_episodes)
         episodesList.extend(self.findEpisodesList(date, json_episodes_object))
         

      #print "EPISODE LIST"
      #print episodesList

      episodesToday = []
      for x in range (0, len(episodesList) - 1):
         #print "STILL ALIVE START"
         episode_details_url = self.makeGetRequest("episodes/", episodesList[x])
         #print episode_details_url
         #print "STILL ALIVE"
         json_episodes_details = self.getJsonResult(episode_details_url)
         #print "STILL ALIVE"
         json_episodes_details_object = json.loads(json_episodes_details)
         #print "STILL ALIVE"
         showToday = self.findEpisodesToday(date, json_episodes_details_object)
         if showToday != "":
            episodesToday.append(showToday)
         #print "STILL ALIVE"

      #print "EPISODES TODAY"
      #print episodesToday
      return str(episodesToday)

   @staticmethod
   def findEpisodesList(date, json_episodes_object):
      episodesForShow = []
      episodesArray = json_episodes_object['response']['Episodes']
      for x in range(0, len(episodesArray) - 1):
         # print "SHORT IDS"
         # print episodesArray[x]['shortId']
         episodesForShow.append(episodesArray[x]['shortId'])

      # print "LALALA:"
      # print episodesForShow
      return episodesForShow

   
   @staticmethod
   def findEpisodesToday(date, json_episodes_details_object):
      #date = "2014-11-06" #Hard coded date to prove that on this day there are results
      # try:
      airdate = (json_episodes_details_object['response']['Episodes'][0]['OriginalAirDate'])[:10]
      #print airdate
      if airdate == date :
         #print "COMAPARISON DONE"
         #print json_episodes_details_object['response']['Episodes']
         try:
            #print str(json_episodes_details_object['response']['Episodes'][0]['Title'])+": "+str(json_episodes_details_object['response']['Episodes'][0]['EpisodeNumber'])
            return str(json_episodes_details_object['response']['Episodes'][0]['Title'])+": Episode "+str(json_episodes_details_object['response']['Episodes'][0]['EpisodeNumber'])
         except:
            #print"Exception Hit"
            return ""
      else :
         #print "COMPARISON FAILED"
         return ""
      # except:
      #    print "FAILED TO TRY"
      #    return ""

   @staticmethod
   def getDate(json_string):
      try:
         date = json_string['outcomes'][0]['entities']['datetime'][0]['from']['value']
      except:
         date = json_string['outcomes'][0]['entities']['datetime'][0]['value']
      return date

   @staticmethod
   def getShowCodes(self):
      #The json_string of all the information is passed in
      #Find all the shortIDs and put them into a showCodes array to be used to access episodes
      show_url = self.makeGetRequest("shows", "")
      json_result = self.getJsonResult(show_url)
      json_result_object = json.loads(json_result)

      showCodes = []
      showArray = json_result_object['response']['Shows']
      for x in range (0, len(showArray) - 1):
         showCodes.append(showArray[x]['shortId'])
      return showCodes

   @staticmethod
   def makeGetRequest(shows, detail):
      contentType = shows
      aspect = detail
      show_url = "http://api.viacom.com/v12/%s%s?apiKey=vT4Aq18ANEmQFPZI4jxFpJFypuGrwmVK " % (contentType, aspect)
      return show_url

   @staticmethod
   def getJsonResult(show_url):
      request = urllib2.Request(show_url)
      result = urllib2.urlopen(request)
      json_result = result.read()
      return json_result
