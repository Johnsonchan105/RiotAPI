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

api_key = "RGAPI-1d1bf699-7b40-418c-bd97-97e75780522c"

summoner_api_url = concat(tft_summoner_api, "IAMABEAN", api_key)

resp = requests.get(summoner_api_url)

playerInfo = resp.json()
#player_accountID = playerInfo["accountId"]
puuid = playerInfo["puuid"]

api_url_matches = match_api(tft_match_history_api, puuid, api_key)

match_api(tft_match_history_api, puuid, api_key)
player_matches = requests.get(api_url_matches)

#list of matches
matches = player_matches.json()
first_match = matches[0]

api_url_match = concat(tft_match_api, first_match, api_key)
match_data = requests.get(api_url_match)
match_info = match_data.json()

metadata = match_info['metadata']

participantsList = metadata['participants']

summonerIndex = participantsList.index(puuid)

participants_match_info  = match_info['info']['participants']

summoner_match_info = participants_match_info[summonerIndex]
print(summoner_match_info)


