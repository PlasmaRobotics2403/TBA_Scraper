import requests
import datetime
import sys

now = datetime.datetime.now()

#API Strings
baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc2403:TBA_Scraper:1.0'}

class tbaParse:
  def __init__(self):
    self.createTime = now
    self.userMessage = "I'm making this __init__ script because I feel like it needs one but it has no real value."

  def getCountryRankings(self):
    country_list = {}

    print("\nLoading Data...")

    for num in range(0,12):
      myRequest = (baseURL + 'teams/' + str(num))
      response = requests.get(myRequest, headers=header)
      jsonified = response.json()

      for team in jsonified:
        country = team["country_name"]

        if not country in country_list:
          country_list[country] = 1
        else:
          old_count = country_list[country]
          new_count = old_count + 1
          country_list[country] = new_count

    organized_list = sorted(country_list.items(), key=lambda x: x[1], reverse=True)

    print("\nFRC-team Country Distribution: (All-teams EVER)")

    ranking = 0
    none_count = 0

    for value in organized_list:
      if not value[0] is None:
        valranking = ranking
        ranking = ranking + 1

        if ranking < 10:
          sanity_marker = " "
        else:
          sanity_marker = ""

        country = value[0]
        teams = value[1]

        print("#" + str(ranking) + sanity_marker + " - " + country + " : " + str(teams))
      else:
        none_count = value[1]

    print("\nTeams without a country: " + str(none_count) + "\n")

parser = tbaParse()
parser.getCountryRankings()
