yhack-smsnow
============
Inspired by the high cost of international roaming, this travel service aims to provide several core phone features to all users. It works regardless of phone OS, or if users have a data/WiFi connection. All info is transmitted via SMS, including user queries and server responses, allowing for easy accessibility when data is not an option.

### Links: ###
* [ChallengePost](http://challengepost.com/software/smsnow-jj1aa)
* [Screenshots](http://yhack-sms.appspot.com/)

### Example phrases: ###
Replace brackets with your search term.

* stock price (GOOG)
* weather (san francisco)
* weather forecast (toronto)
* set alarm (8am tomorrow)
* remind me (pay the phone bill)
* translate "(phrase)" (korean)
* directions from (yale university) to (harvard university)
* attractions near (Los Angeles Convention Center)
* find hotel near (Yale University)
 
## Setup ##
Download the [Python Google App Engine SDK for Linux](https://cloud.google.com/appengine/downloads) and unzip it to get the `google_appengine` folder. Clone the repository.  
Rename `APIKeys_template.py` to `APIKeys.py` and fill in your API keys.  
Place your info in `app.yaml`

#### Install Dependencies ####
First, `cd` into the project directory.  
Install `virtualenv` with `sudo easy_install pip`, then `sudo pip install virtualenv`  
Set up a virtual environment: `virtualenv --distribute venv`  
Activate it: `source venv/bin/activate`  
Install twilio and dateutil: `pip install twilio` and `pip install python-dateutil`  
Deactivate virtual environment: `deactivate`  
Link dependencies to your project:
```
ln -s venv/lib/python2.7/site-packages/twilio .
ln -s venv/lib/python2.7/site-packages/httplib2 .
ln -s venv/lib/python2.7/site-packages/six.py .
ln -s venv/lib/python2.7/site-packages/dateutil .
```

Now, you can run the project locally with `./dev_appserver.py <path_to_project>`  
or deploy it with `./appcfg.py update <path_to_project>`
