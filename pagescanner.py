#!/usr/bin/python

import sys
import urllib2
import re
import csv

list1 = []

def getAddress():
	url = raw_input("Site to scrape: ")
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseAddress():
	try:
		website = urllib2.urlopen(getAddress())
		html = website.read()

		addys = re.findall('''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', html, flags=re.IGNORECASE)

		global list1
		list1.append(addys)

	except urllib2.HTTPError, err:
		print "Cannot retrieve URL: HTTP Error Code: ", err.code
	except urllib2.URLError, err:
		print "Cannot retrive URL: " + err.reason[1]

def execute():
	parseAddress()
	

### MAIN

def main():
	execute()
	global list1
	myFile = open("finishedFile.csv", "w+")
	wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
	wr.writerow(list1)
	myFile.close
	
main()
