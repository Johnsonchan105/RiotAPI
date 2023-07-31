import requests
api_key = "RGAPI-4dac3abd-984a-4a36-b864-696c2ca164e8"
api_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/IAMABEAN"
api_url = api_url + "?api_key=" + api_key
resp = requests.get(api_url)
resp.json()

