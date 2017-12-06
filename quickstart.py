import os
import re
from flask import Flask, jsonify, render_template, request

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# Configure application
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

@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        console.log(request.form.get("link"))
        # Redirect user to home page
        return redirect(request.form.get("link"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")



# def get_authenticated_service():
#   flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#   credentials = flow.run_console()
#   return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
#
# def channels_list_by_username(service, **kwargs):
#   results = service.channels().list(
#     **kwargs
#   ).execute()
#
#   print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
#        (results['items'][0]['id'],
#         results['items'][0]['snippet']['title'],
#         results['items'][0]['statistics']['viewCount']))

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  # service = get_authenticated_service()
  # channels_list_by_username(service,
  #     part='snippet,contentDetails,statistics',
  #     forUsername='GoogleDevelopers')
