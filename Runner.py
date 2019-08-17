from time import sleep

from OpenDota import getLastMatch
from LastMatchInformation import LastMatchInformation
from Twitter import makeAndPost

while True:
    previous_match = ""
    lmi = getLastMatch(LastMatchInformation())

    hashtags = "#TI9 #DOTA2 #OpenDota"

    message = "Just " + lmi.win + " as " + lmi.hero + " as " + lmi.lane + " and got " + str(lmi.kills) + " kills. "\
              + "Match was played " + str(lmi.time) + ". Match report: https://www.opendota.com/matches/" + str(lmi.match_id) \
              + " " + hashtags

    if previous_match != lmi.match_id:
        makeAndPost(message)
        print(message)

    previous_match = lmi.match_id

    sleep(900)

