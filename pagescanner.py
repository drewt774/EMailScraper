#PageScanner 0.2
#Drew Taylor, forked from Kirk Durbin


import sys
import urllib2
import re
import csv

list1 = []
list2 = []
list3 = []

def addList():
	with open('file.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			for s in row:
				list2.append(s)

def getAddress(url):
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseAddress(url):
	global list3
	try:
		website = urllib2.urlopen(getAddress(url))
		html = website.read()

		addys = re.findall('''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', html, flags=re.IGNORECASE)

		global list1
		list1.append(addys)

	except urllib2.HTTPError, err:
		print "Cannot retrieve URL: HTTP Error Code: ", err.code
		list3.append(url)
	except urllib2.URLError, err:
		print "Cannot retrive URL: " + err.reason[1]
		list3.append(url)

def execute():
	global list2
	addList()
	totalNum = len(list2)
	atNum = 1
	for s in list2:
		parseAddress(s)
		print "Processing " + str(atNum) + " out of " + str(totalNum)
		atNum = atNum + 1

	print "Completed. Emails parsed: " + str(len(list1)) + "."


### MAIN

def main():
	global list2
	execute()
	global list1
	myFile = open("finishedFile.csv", "w+")
	wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
	for s in list1:
		wr.writerow(s)
	myFile.close
	global list3
	failFile = open("failedSites.csv", "w+")
	write = csv.writer(failFile, quoting=csv.QUOTE_ALL)
	for j in list3:
		write.writerow(j)
	failFile.close

main()
