#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Filename:   enviar-examens.py
Author:     Rafel Amer (rafel.amer AT upc.edu)
Copyright:  Rafel Amer 2020--2024
Disclaimer: This program is provided "as is", without warranty of any kind,
            either expressed or implied, including, but not linmited to, the
            implied warranties of merchantability and fitness for a particular
            purpose.
            It has been written to generate random models of exams for the
            subject of Linear Algebra at ESEIAAT, Technic University of Catalonia
License:    This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU General Public License as published by
            the Free Software Foundation, either version 3 of the License, or
            (at your option) any later version.

 	        See https://www.gnu.org/licenses/
"""

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

import filetype
import mimetypes
import os.path
import base64
import pandas
import mimetypes
import sys
import re
import unidecode
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from googleapiclient.errors import HttpError
from optparse import OptionParser
try:
  from pandas_ods_reader import read_ods
except:
  print ("Can't import pandas_ods_reader")

parser = OptionParser()
parser.add_option("--estudiants",dest="estudiants",default=None)
parser.add_option("--full",dest="full")
parser.add_option("--subject",dest="subject",default=None)
parser.add_option("--message",dest="message",default=None)
parser.add_option("--sender",dest="sender",default=None)
parser.add_option("--carpeta",dest="carpeta",default="tex")
parser.add_option("--ajuda",action="store_true",dest="ajuda",default=False)
parser.add_option("--solucions",action="store_true",dest="solucions",default=False)
(options,args) = parser.parse_args()
#
#
#
def estudiants_from_ods(file):
    result = []
    for e in file.values:
        try:
            if e[5] == 0:
                continue
        except:
            pass
        try:
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'email'   : e[3],
                     'grup'    : e[4] 
                    }
            result.append(dades)
        except:
            pass
    return result
#
#
#
def estudiants_from_excel(file):
    result = []
    for index, e in file.iterrows():
        try:
            if e[5] == 0:
                continue
        except:
            pass
        try:
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'email'   : e[3],
                     'grup'    : e[4] 
                    }
            result.append(dades)
        except:
            pass
    return result
#
#
#
def estudiants_from_csv(file):
    regex = re.compile(r'^\s*#.*$',re.IGNORECASE)
    result = []
    count =  0
    for e in file:
        if len(e) > 0:
            count += 1
        e = e.strip()
        if regex.match(e):
            continue
        try:
            e = e.split(':')
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'email'   : e[3],
                     'grup'    : e[4] 
                    }
            result.append(dades)
        except:
            pass
    return result
#
#
#
def create_message(sender,to,subject,message_text,files):
    """Create a message for an email.
    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        files: List of the paths to the files to be attached.
    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    for file in files:
        content_type, encoding = mimetypes.guess_type(file)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(msg)
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
    return {'raw': base64.urlsafe_b64encode(bytes(message.as_string().encode('utf-8'))).decode("ascii")}
#
#
#
def send_message(service, user_id, message):
    """
    Send an email message.
    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
        message: Message to be sent.

    Returns:
        Sent Message.
    """
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print ('Message Id: %s' % message['id'])
    except HttpError as error:
        print ('An error occurred: %s' % error)

HOME = os.path.expanduser('~')
est = options.estudiants
fitxer = options.message
carpeta = options.carpeta
full = options.full
try:
    full = int(full)
except:
    pass
if full is None:
    full = 0
sender, subject = options.sender,options.subject
if sender is None or subject is None:
    print("S'ha d'especificar l'assumpte i l'emisor dels correus")
    sys.exit(0)

if est is not None:
    try:
        kind = filetype.guess(options.estudiants)
        if kind is not None and kind.mime == 'application/vnd.oasis.opendocument.spreadsheet':
            f = read_ods(est,full,headers=False)
            estudiants = estudiants_from_ods(f)
        elif kind is not None and kind.mime in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                'application/vnd.ms-excel']:
            f = pandas.read_excel(est,full,header=None)
            estudiants = estudiants_from_excel(f)
        else:
            f = open(est,"r",encoding='utf8')
            estudiants = estudiants_from_csv(f)
            f.close()
    except:
        print("Error de lectura del fitxer d'estudiants")
        sys.exit(0)

try:
    with open(fitxer,'r') as f:
        message = f.read()
except:
    print("Error de lectura del fitxer amb el missatge del correu")
    sys.exit(0)

try:
    tokenfile = os.path.join(f"{HOME}","credentials","token.json")
    creds = Credentials.from_authorized_user_file(tokenfile, SCOPES)
except:
    print(f"Error en llegir el fitxer {tokenfile}")
    sys.exit(0)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        credentials = os.path.join(f"{HOME}","credentials","credentials.json")
        flow = InstalledAppFlow.from_client_secrets_file(credentials, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(tokenfile,'wb') as token:
            pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

for e in estudiants:
    relacio = {'COGNOMS' : e['cognoms'], 'NOM' : e['nom']}
    m = message
    for k,v in relacio.items():
        m = m.replace(k,v)
    filename = os.path.join(carpeta,f"{e['cognoms']}-{e['nom']}".lower().replace(' ','-'))
    filename = unidecode.unidecode(filename)
    filename = filename.replace("'","")
    if options.solucions:
        filename += "-solucio.pdf"
    else:
        filename += ".pdf"
    correu = create_message(sender,e['email'],subject,m,[filename])
    send_message(service,'me', correu)
    time.sleep(0.5)
