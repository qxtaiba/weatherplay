from flask import Flask, request, render_template, url_for
import os, json, requests
import flaskapp.secret as secret
# import utils.(filename)

app = Flask(__name__)

positionData = {}

@app.route('/')
def show_page(): 
    return render_template("index.html") 

@app.route('/logged')
def show_another():
    # get the auth portion of url
    code = request.args['code']
    print("spotify code", code)

    # make a post to spotify auth
    tokens = get_spotify_token(code)


    # get the spotify auth related tokens
    access_token = tokens['access_token']

    # use location data to make the weather api call
    # keywords = get_weather_keyword(lat, lon)

    # use weather data to create a spotify playlist
    
    # store the id of the playlist. use the playlist id to play on speaker
    playlist_id = ""
    # requests.post
    return "Hello"

def get_spotify_token(code):
    url = "https://accounts.spotify.com/api/token"
    payload = {"grant_type": "authorization_code", "code": code, "redirect_uri":"localhost:5000/logged", 
        "client_id": secret.CLIENT, 
        "client_secret": secret.CLIENT_SECRET}
    res = requests.post(url, data=payload)
    resjson = res.json()
    print("RESPONSE FOR TOKEN REQUEST", resjson)
    return json.loads(resjson)

def get_weather_keyword(lat, lon):
    pass
    url = ""
    params = {"lat": "", "lon": ""}
    # res = requests.get(url, params=params)
    # print(res.json)
    summary = ""
    return summary

@app.route('/getLocation', methods = ['POST'])
def getLocationData():
  res = request.json
  print(res)
  return res