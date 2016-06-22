import requests
import datetime
import sys

now = datetime.datetime.now()

#API Strings
baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc1257:thepythonalliance:beta'}

class tbaParse:
  def __init__(self):
    self.createTime = now
    self.userMessage = "I'm making this __init__ script because I feel like it needs one but it has no real value."
  
  def getCountryRankings(self):
    country_list = {}
    
    for num in range(0,12)
      myRequest = (baseURL + 'teams/' + num)
      response = requests.get(myRequest, headers=header)
      jsonified = response.json()
      
      for team in jsonified:
        country = team["country-name"]
       
        if not country in countryList:
          country_list[country] = 1
        else:
          old_count = country_list[country]
          new_count = old_count + 1
          country_list[country] = new_count
    
    organized_list = sorted(country_list.items(), key=lambda x: x[1])
    
    print("\nFRC-team Country Distribution: (All-teams EVER)")
    
    for key,value in organized_list:
      ranking = key + 1
      
      if ranking < 10:
        sanity_marker = " "
      else:
        sanity_marker = ""
      
      print ranking, sanity_marker, ": ", value

parser = tbaParse()
parser.getCountryRankings()
