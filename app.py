import os
import json
from urllib2 import urlopen
from flask import Flask, render_template, request, redirect
import requests
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# main function
@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "POST":

        # get desired file format
        mp3 = True
        if request.form.get("format") == "mp4":
            mp3 = False

        # get playlist id from url
        playlist = request.form.get("link")[(request.form.get("link").index("list=") + 5)::]
        if (playlist.find('/') != -1):
            playlist = playlist[::playlistId.index('/')]

        # read playlist data
        getURL = "https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId=" + playlist + "&key=AIzaSyBs7FSXDVi_wTw1Nn2LHEMxt2eAWMuErfY"
        page = urlopen(getURL)
        data = json.loads(page.read())

        videos = []
        lastPage = False

        # ensure all pages of the data are visited
        while not lastPage:
            for i in data['items']:
                # get id of all videos in playlist
                videos.append("https://www.youtube.com/watch?v=" + i["contentDetails"]["videoId"])
            try:
                nextPage = data["nextPageToken"]
                data = json.loads(urlopen(getURL + "&pageToken=" + nextPage).read())
            except:
                lastPage = True

        # check start/end for downloads
        try:
            start = int(request.form.get("start"))
        # no input so start at beginning of playlist
        except:
            start = 0
        try:
            end = int(request.form.get("end"))
        # no input so end with last song in playlist
        except:
            end = len(videos)

        for i in range(start, end):
            # in case of deleted/unaccesible videos
            try:
                if mp3:
                    # access command line
                    print subprocess.check_output(["youtube-dl","--extract-audio", "--audio-format", "mp3", "%s" % (videos[i])])
                else:
                    print subprocess.check_output(["youtube-dl","%s" % (videos[i])])
            except:
                continue

    return render_template("index.html")

if __name__ == '__main__':
  app.run('localhost', 8090, debug=True)
