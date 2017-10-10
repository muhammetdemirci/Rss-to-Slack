# -*- coding: utf-8 -*-
# @muhammetdemirci
import urllib2
import untangle
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import os 
import time

reload(sys)
sys.setdefaultencoding('utf-8')

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

past_post_links = []

url = "http://www.*****.com/rss/"
slack_webhook_url = "https://hooks.slack.com/services/********" 

while(1):
  page = ""
  try:
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    page = response.read()
  except ValueError:
    print("error : ")

 
#print(page)
 
obj = untangle.parse(page)
 
 
for item in obj.rss.channel.item:
 
  
  if item.link.cdata not in past_post_links:
    text = """curl -X POST -H 'Content-type: application/json' --data '{"text":" @here """ + item.title.cdata + " " + item.link.cdata +"\"}'""" + slack_webhook_url
    os.system(text)
    print("sending : ",text)

  past_post_links.append(item.link.cdata)
 
  
 
time.sleep(10000)
 
response.close() # its always safe to close an open connection
