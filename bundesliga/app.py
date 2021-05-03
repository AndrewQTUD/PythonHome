import requests

url = "https://heisenbug-bundesliga-live-scores-v1.p.rapidapi.com/api/bundesliga/match/events"

querystring = {"team1": "Schalke 04", "team2": "Hannover 96"}

headers = {
    'x-rapidapi-key': "74eb512be4mshfd566891df88c1fp1727e9jsn849c978244c2",
    'x-rapidapi-host': "heisenbug-bundesliga-live-scores-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
