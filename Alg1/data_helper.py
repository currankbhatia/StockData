import urllib2
from yahoo_finance import Share
import numpy as np
import csv
from collections import defaultdict
import time
from urllib2 import urlopen
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import pandas_datareader.data as web
#import Series
import pandas

def date_translator(str_date):


    yr = int(str_date[0:4])
    month = int(str_date[5:7])
    day = int(str_date[8:10])

    return date(yr, month, day)

#used to be called get_google_data
def get_historical_data(startTime, endTime, shareName):

    try:
        x = web.DataReader(shareName, "yahoo", date_translator(startTime),date_translator(endTime))
    except:
        print "Passed one, that did not have data"
        return False


    #print x


    dates1 = x.index.tolist()
    close1 = x['Close'].tolist()

    dates_t = list()

    for i in range(len(close1)):
        mystr = str(dates1[i])
        dates_t.append(date_translator(mystr[0:10]))
   
    #for i in range(len(close1)):
        #print "Date: {}, Close: {}".format(dates_t[i], close1[i])

    #str1 = str(dates1[0])
    #print str1
    #print str1[0:10]
    #print date.fromtimestamp(dates1[0])

    return [dates_t, close1]


def old_get_historical_data(startTime, endTime, shareName):
    stock = Share(shareName)
    data = stock.get_historical(startTime, endTime)
    return data

def print_historical_data(data):
    for i in range(len(data)):
        print '{} and {}'.format(data[i]['Adj_Close'], data[i]['Date'])

def print_list(list1):
    for i in range(len(list1)):
        print list1[i]

#prints  a number of lists at the same time
def print_lists(lists):
   
    arr = np.array(lists)
    array = np.transpose(arr)
    for i in range(len(array)):
        print array[i]

#Returns a list of data with Adj_Close and Date
def data_list(data): 
    retData = []
    for i in range(len(data)):

        
        str1 = data[i]['Date'] 

        yr = int(str1[0:4])
        month = int(str1[5:7])
        day = int(str1[8:10])
        #print '{}, {}. {}'.format(yr, month, day)
        
        
        retData.append([data[i]['Adj_Close'], date(yr, month, day)])

    return retData

#presents data as individual lists and reverses them for readability of data
def data_lists_reversed(data):
    dataLs = data_list(data)
    dataLs.reverse()
    priceLs = [x[0] for x in dataLs] #list comprehension
    datesLs = [x[1] for x in dataLs]
    return [dataLs, priceLs, datesLs]

def plot_data_xy(x, y):

    plt.figure()
    plt.plot_date(x, y, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()


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
    plt.figure()
    plt.plot_date(dateList, adjList, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()

#------ Start of script ---------
#startTime = "2005-01-01"
#endTime = "2005-10-10" 
#print date_translator("2005-10-22")

#get_google_data("2016-01-01", "2017-03-02","TSLA")

#data = get_historical_data(startTime, endTime, '^GSPC')

#print "---"

