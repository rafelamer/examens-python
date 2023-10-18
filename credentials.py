#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#
# If modifying these scopes, delete the file token.pickle.
#
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    creds = None
    HOME = os.path.expanduser('~')
    #
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    #
    tokenfile = os.path.join(f"{HOME}","credentials","token.pickle")
    if os.path.exists(tokenfile):
        with open(tokenfile,'rb') as token:
            creds = pickle.load(token)
    #
    # If there are no (valid) credentials available, let the user log in.
    #
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            credentials = os.path.join(f"{HOME}","credentials","credentials.json")
            flow = InstalledAppFlow.from_client_secrets_file(credentials,SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tokenfile,'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

if __name__ == '__main__':
    main()
