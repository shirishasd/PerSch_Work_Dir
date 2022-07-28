import base64
from base64 import decode
import json
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import spotipy.util
from secret import * ##(cid ,secret)
##dotenv.config({path: "/.env"})
#Authentication - without user -- from the gitignore file
#client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Step 1 - Authorization
authurl = "https://accounts.spotify.com/api/token"
authheaders = {}
authdata = {}

# Encode as Base64
message = f"{cid}:{secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')
print(base64Message)

authheaders['Authorization'] = f"Basic {base64Message}"
authdata['grant_type'] = "client_credentials"

#print(authheaders)
#print(authdata)

res = requests.post(authurl, headers=authheaders, data=authdata)
print(res)
print(json.dumps(res.json(), indent=2))
token = res.json()['access_token']
print(token)


