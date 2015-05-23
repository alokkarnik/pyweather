#!/usr/bin/python


def main():
	import urllib2
	import json	
	import sys

	city = sys.argv[-1]

	url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + city + "%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	#Create object of the URL
	obj = urllib2.urlopen(url)

	#Pull the current data
	data = json.load(obj)


	title = data['query']['results']['channel']['item']['title']
	city = data['query']['results']['channel']['location']['city']
	country = data['query']['results']['channel']['location']['country']
	date = data['query']['results']['channel']['item']['condition']['date']
	faren = data['query']['results']['channel']['item']['condition']['temp']
	weather = data['query']['results']['channel']['item']['condition']['text']

	print "\n"
	print "Conditions for",city,country
	print date
	print "Temperature:",(((int(faren) - 32)) * 5/9 )
	print "Weather:",weather

	print "\n"
	

if __name__ == '__main__':
	main()
	
