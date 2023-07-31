import requests

#match list(4 query parameters)
def match_api(api_link, val, key, start = 0, endTime = None, startTime = None, count=20):
    temp = api_link + val + "/ids?"
    temp += "start=" + str(start)
    if endTime:
        temp += "&endTime=" + str(endTime)
    if startTime:
        temp += "&startTime=" + str(startTime)
    temp += "&count=" + str(count)
    temp += "&api_key=" + api_key
    return temp
    

#single query parameter
def concat(api_link, val, key):
    if "?" in api_link:
        return api_link + val + "&api_key=" + api_key
    return api_link + val + "?api_key=" + api_key 


#concat summoner name
tft_summoner_api = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"
#concat puuid (find from summoner name)
tft_match_history_api = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"
#concat match from match history
tft_match_api = "https://americas.api.riotgames.com/tft/match/v1/matches/"

api_key = "RGAPI-4dac3abd-984a-4a36-b864-696c2ca164e8"

summoner_api_url = concat(tft_summoner_api, "IAMABEAN", api_key)

resp = requests.get(summoner_api_url)

playerInfo = resp.json()
player_accountID = playerInfo["accountId"]
puuid = playerInfo["puuid"]

api_url_matches = match_api(tft_match_history_api, puuid, api_key)
match_api(tft_match_history_api, puuid, api_key)
player_matches = requests.get(api_url_matches)
matches = player_matches.json()
print(matches)
