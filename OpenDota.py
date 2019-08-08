import requests
import time
import json

account_id = "14367619"
api_base = "https://api.opendota.com/api"


# Get last match
def getLastMatch():
    r = requests.get(url=api_base + "/players/" + account_id + "/recentMatches/")
    data = r.json()
    return data[0]["match_id"]


# Get lane role
def getLaneRole(lane_role):
    #1-4 (Safe, Mid, Off, Jungle)
    return {
        "1": "Safelane",
        "2": "Midlane",
        "3": "Offlane",
        "4": "Jungle"
    }.get(lane_role, "Support")


# Get hero name
def getHero(hero_id):
    #r = requests.get(url=api_base + "/heroes")
    #data = r.json()
    #print(data)

    #All the heroes
    with open('Heroes.json', "r") as f:
        data = json.load(f)
    print(data)
    #Find Hero in JSON
    for i in data:
        if hero_id == i["id"]:
            return i["localized_name"]


# Get time of match
def getTimeAndDate(start_time):
    return time.strftime("%H:%M:%S @ %d.%m.%Y", time.localtime(start_time))


# Did you win? If true then yes, if false then no
def winOrLose(player_slot, radiant_win):
    #Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
    if player_slot < 128 and radiant_win == "true":
        return True
    else:
        return False


print(winOrLose(0, "false"))
