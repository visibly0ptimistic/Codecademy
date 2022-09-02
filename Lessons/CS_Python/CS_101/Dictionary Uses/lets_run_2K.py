# import the random module to generate a random number
import random

# A dictionary containing all 30 NBA teams
# teams = {key: value}
teams = { 1: "Atlanta Hawks", 2:	"Boston Celtics", 3: "Brooklyn Nets", 4: "Charlotte Hornets", 5: "Chicago Bulls", 6: "Cleveland Cavaliers", 7: "Dallas Mavericks", 8: "Denver Nuggets", 9: "Detroit Pistons", 10: "Golden State Warriors", 11: "Houston Rockets", 12: "Indiana Pacers", 13: "Los Angeles Clippers", 14:	"Los Angeles Lakers", 15: "Memphis Grizzlies", 16: "Miami Heat", 17: "Milwaukee Bucks", 18:	"Minnesota Timberwolves", 19: "New Orleans Pelicans", 20: "New York Knicks", 21: "Oklahoma City Thunder", 22: "Orlando Magic", 23: "Philadelphia 76ers", 24: "Phoenix Suns", 25: "Portland Trail Blazers", 26: "Sacramento Kings", 27: "San Antonio Spurs", 28: "Toronto Raptors", 29: "Utah Jazz", 30: "Washington Wizards"}

# create an empty dictionary to store team selections
selections = {}

# Here 3 items are added to the empty dictionary selections
# The empty dictionary (selections) is assigned a key (first team, second team, third team)
# Then a random key from the teams dictionary is selected.
# The item (key: value) is removed from the teams list and it's value is assigned to the selections key (first team, second team, third team)
selections["first team"] = teams.pop(random.randint(1, 30))
selections["second team"] = teams.pop(random.randint(1, 30))
selections["third team"] = teams.pop(random.randint(1, 30))

# Here I loop through selections dictionary and print a statement to the console which displays the teams and the order they were selected. 
for key, value in selections.items():
    print("Your " + key + " is the " + value + ".")