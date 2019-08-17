import requests
import time
import json
from LastMatchInformation import LastMatchInformation
from Configuration.OpenDotaConfiguration import account_id

account_id = account_id
api_base = "https://api.opendota.com/api"


# Get last match
def getLastMatch(lmi):
    lmi = LastMatchInformation()
    r = requests.get(url=api_base + "/players/" + account_id + "/recentMatches/")
    data = r.json()

    lmi.match_id = data[0]["match_id"]
    lmi.kills = data[0]["kills"]
    lmi.time = getTimeAndDate(data[0]["start_time"])
    lmi.win = winOrLose(data[0]["player_slot"], data[0]["radiant_win"])
    lmi.lane = getLaneRole(data[0]["lane_role"])
    lmi.hero = getHero(data[0]["hero_id"])

    return lmi


# Get lane role
def getLaneRole(lane_role):
    #1-4 (Safe, Mid, Off, Jungle)
    return {
        1: "safelane",
        2: "midlane",
        3: "offlane",
        4: "jungle"
    }.get(lane_role, "support")


# Get hero name
def getHero(hero_id):
    #r = requests.get(url=api_base + "/heroes")
    #data = r.json()
    #print(data)

    #All the heroes
    with open('Heroes.json', "r") as f:
        data = json.load(f)

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
        return "lost"
    else:
        return "won"
