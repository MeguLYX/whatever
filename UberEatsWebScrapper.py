# LONG - COMP112-01 - FINAL PROJECT

# Importing Required Libraries 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import requests

# Creating Classes 
class Restaurant:
     def __init__(self, restaurant_id, restaurant_name, rating, cuisine):
          self.id = restaurant_id
          self.name = restaurant_name
          self.rating = rating 
          self.cuisine = cuisine

class Category:
     def __init__(self, category_id, category_name, category_group):
          self.id = category_id
          self.name = category_name
          self.group = category_group

# Determining which city and state the user is in 
city = input("Please enter the name of a city: ").replace(" ", "-")
state = input("Enter the abbreviation/name of your state: ")
# US States dictionary that has full state names as keys, two-word abbreviations for values
us_states = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY",
    "district of columbia": "DC",
    "american samoa": "AS",
    "guam": "GU",
    "northern mariana islands": "MP",
    "puerto rico": "PR",
}
# If user enters state name instead of abbreviation, the following code translates that into an abbreivation 
if len(state) > 2: 
     state1 = state.lower()
     if state1 in us_states.keys():
          state = us_states[state1]
     else: 
          input("Please enter a valid US State!")

# Creating the URL using the user's info  
url = "https://www.ubereats.com/city/" + city.lower() + "-" + state.lower()
# Sending a request to the page 
req = Request(url)
# Getting contents of the webpage 
try:
     webpage = urlopen(req).read()
except HTTPError:
     print("You might've entered some info wrongly! Please check again!")

# use BeautifulSoup to parse the webpage
soup = BeautifulSoup(webpage, 'html.parser')

# Lists for compiling all the info scrapped:
restaurant_list = []
rating_list = []
cuisine_list = []
data = {}

# By using Inspect Element, we can see that UberEats uses <h3> tag to identify restaurant names
# Therefore, we can use the <h3> tag to get all the restaurants available
for x in soup.findAll("h3")[:80]: 
     restaurant_name = x.get_text()
     restaurant_list.append(restaurant_name)
     rating = soup.find("div", text = restaurant_name).findNext("div").text 
     rating_list.append(rating)
     cuisine = []
     for child in x.parent.parent.find("span").parent:
          content = child.text.replace('\xa0•\xa0',"")
          if content == "":
               continue
          cuisine.append(content) 
     cuisine_list.append(cuisine)


# Compiling all the 3 lists together into a dictonary 
for i, restaurant in enumerate(restaurant_list):
     data = {}
     data[restaurant] = {
          "Food Genre": cuisine_list[i],
          "Rating": rating_list[i]
     }
     print(data)

