import os
import re
from flask import Flask, jsonify, render_template, request, redirect

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask(__name__)

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "POST":
        playlistId = request.form.get("link")[(request.form.get("link").index('=') + 1)::]
        if (playlistId.find('/') != -1):
            playlistId = playlistId[::playlistId.index('/')]

        playlist_items_list_by_playlist_id(client,
            part='snippet,contentDetails',
            maxResults=25,
            playlistId=playlistId)

        return redirect(request.form.get("link"), code=302)
    else:
        return render_template("index.html")


def playlist_items_list_by_playlist_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().list(
    **kwargs
  ).execute()

  return print_response(response)

# @app.route("/members")
# def members():
#     return "Members"
#
# @app.route("/members/<string:name>/")
# def getMember(name):
#     return name

### ORIGINAL CODE FROM GOOGLE QUICKSTART

# def channels_list_by_username(service, **kwargs):
#   results = service.channels().list(
#     **kwargs
#   ).execute()
#
#   print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
#        (results['items'][0]['id'],
#         results['items'][0]['snippet']['title'],
#         results['items'][0]['statistics']['viewCount']))

### ALTERNATIVE

# if __name__ == "__main__":
#     app.run()

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  # service = get_authenticated_service()
  # channels_list_by_username(service,
  #     part='snippet,contentDetails,statistics',
  #     forUsername='GoogleDevelopers')
