# By : Kris Khundrakpam on 15/May/2019

import tweepy
import time
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

TEXT_FILE_NAME = 'fixed_text.txt'

def retrieve_text(file_name):
    f_read = open(file_name, 'r')
    text = f_read.read()
    f_read.close()
    return text

def reply():

    print('Copy-Paste the URL of tweet you want to reply to:')
    url = str(input())
    temp = url.replace('https://twitter.com/','')
    user, useless, _id = temp.split('/')  #All tweet links are divided into username, status and id sections

    text = retrieve_text(TEXT_FILE_NAME)

    api.update_status(  'Replied: @' + user + '(@username)' + ' ' + text + '(Pre-set text from text file)', in_reply_to_status_id = _id)
    

reply()