import os
import re
from flask import Flask, jsonify, render_template, request, redirect, session
# import urllib.request
import requests
# import flask

# import google.oauth2.credentials
# import google_auth_oauthlib.flow
# import googleapiclient.discovery

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

app = Flask(__name__)

# app.secret_key = os.urandom(24)
#
# # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# # the OAuth 2.0 information for this application, including its client_id and
# # client_secret.
# CLIENT_SECRETS_FILE = "client_secret.json"
#
# # This OAuth 2.0 access scope allows for full read/write access to the
# # authenticated user's account and requires requests to use an SSL connection.
# SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
# API_SERVICE_NAME = 'youtube'
# API_VERSION = 'v3'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "POST":
        playlist = request.form.get("link")[(request.form.get("link").index("list=") + 5)::]
        if (playlist.find('/') != -1):
            playlist = playlist[::playlistId.index('/')]
        # print(playlist)

        getURL = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=25&playlistId=" + playlist + "&key=AIzaSyBs7FSXDVi_wTw1Nn2LHEMxt2eAWMuErfY"

        r = requests.get(getURL)
        print r.content

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


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  app.run('localhost', 8090, debug=True)
