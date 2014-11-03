import json
import urllib2
import urllib
from APIKeys import GoogleApiKey

class GetTranslate():
   @staticmethod
   def gettranslate(json_string):
      phrase = json_string['outcomes'][0]['_text']
      phrase = phrase.split("\"")[1]
      language = json_string['outcomes'][0]['_text']
      wordList = language.split(" ")
      language = wordList[-1].lower()

      locale = "en"
      if language == "french":
         locale = "fr"
      elif language == "german":
         locale = "de"
      elif language == "spanish":
         locale = "es"
      elif language == "japanese":
         locale = "ja"
      elif language == "chinese":
         locale = "zh"
      elif language == "italian":
         locale = "it"
      elif language == "korean":
         locale = "ko"
      elif language == "dutch":
         locale = "nl"
      elif language == "czech":
         locale = "cs"
      elif language == "russian":
         locale = "ru"
      elif language == "romanian":
         locale = "ro"
      else:
         locale = "en"

      phrase = urllib.quote(phrase)
      api_url = "https://www.googleapis.com/language/translate/v2?key="+GoogleApiKey+"&target="+locale+"&q="+phrase

      request = urllib2.Request(api_url)
      response = urllib2.urlopen(request)
      json_result = response.read()
      json_object_result = json.loads(json_result)
      translate_phrase = json_object_result['data']['translations'][0]['translatedText']

      return translate_phrase
