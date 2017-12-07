import os
import re
import json
import urllib
from urllib2 import urlopen
from flask import Flask, jsonify, render_template, request, redirect, session
import requests
import subprocess

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from errno import EPIPE

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "POST":
        playlist = request.form.get("link")[(request.form.get("link").index("list=") + 5)::]
        if (playlist.find('/') != -1):
            playlist = playlist[::playlistId.index('/')]

        getURL = "https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId=" + playlist + "&key=AIzaSyBs7FSXDVi_wTw1Nn2LHEMxt2eAWMuErfY"
        page = urlopen(getURL)
        data = json.loads(page.read())

        videos = []
        lastPage = False

        # check if nextPageToken exists. If so, add &pageToken= XX and call page again
        while not lastPage:
            try:
                nextPage = data["nextPageToken"]
                data = json.loads(urlopen(getURL + "&pageToken=" + nextPage).read())
            except:
                lastPage = True

            for i in data['items']:
                videos.append(i["contentDetails"]["videoId"])
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
