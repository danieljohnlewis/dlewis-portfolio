import csv
import urllib2, urllib
import time

url = 'https://docs.google.com/spreadsheet/pub?key=0AkXKM3uHb4ahdG55S1hkUEpwYi1KaE1lRjI5V3drNnc&single=true&gid=0&output=csv'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request)

reader = csv.reader(response)

''' THEN WE DO SOMETHING USEFUL WITH THE DATA '''
