import urllib2
from yahoo_finance import Share
import numpy
import csv
from collections import defaultdict
import time
from urllib2 import urlopen

""" Algorithm: Find high inflection points in SP500 and compare it to prices of stocks in other industries """

def get_historical_data(startTime, endTime, shareName):

    stock = Share(shareName)
    data = stock.get_historical(startTime, endTime)
    return data



startTime = "2005-01-01"
endTime = "2005-01-10" 

data = get_historical_data(startTime, endTime, '^GSPC')

print "---"
print data[0]['Adj_Close']
print data[0]['Date']

