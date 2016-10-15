import urllib2
from yahoo_finance import Share
import numpy
import csv
from collections import defaultdict
import time
from urllib2 import urlopen
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date



def get_historical_data(startTime, endTime, shareName):
    stock = Share(shareName)
    data = stock.get_historical(startTime, endTime)
    return data

def print_historical_data(data):
    for i in range(len(data)):
        print '{} and {}'.format(data[i]['Adj_Close'], data[i]['Date'])


def plot_data(data):

    adjList = []
    dateList = []
    for i in range(len(data)):
        adjList.append(data[i]['Adj_Close'])
        str1 = data[i]['Date'] 

        yr = int(str1[0:4])
        month = int(str1[5:7])
        day = int(str1[8:10])
        #print '{}, {}. {}'.format(yr, month, day)
        dateList.append(date(yr, month, day))
    #print adjList
    #print dateList

    plt.plot_date(dateList, adjList, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()


startTime = "2005-01-01"
endTime = "2005-10-10" 

data = get_historical_data(startTime, endTime, '^GSPC')

print "---"

plot_data(data)
