

import matplotlib.pyplot as plt
import numpy as np
import csv

import data_helper as dh
import aroon as an

from datetime import datetime, timedelta



def addDays(dateStr, daysR):

    start = datetime.strptime(dateStr, "%Y-%m-%d")
    newDate = start + timedelta(days=daysR)
    newDateStr = str(newDate.date())
    return newDateStr


def gain(stockName, endDate, days):

    ret = dh.get_historical_data(endDate, addDays(endDate, days), stockName)
    prices = ret[1]
    return round(prices[len(prices)-1] - prices[0], 3)
    

def dayGains(stocks, endDate, days):

    effective = 0
    for x in stocks:
        diff = gain(x, endDate, days)
    
        print "{}: {}".format(x, diff)
        if diff > 0:
            effective = effective + 1
        
    succRate = float(effective)/len(stocks)
    print "The success rate is : " + str(succRate)


def multDaysTests(stocks, endDate):

    lsTop = ["Company", 5,10,20,30,60,90,120,180,240,300,360]
    lsStockGains = []
    for x in stocks:
        ls = []
        ls.append(x)
        ls.append(gain(x, endDate,5))
        ls.append(gain(x, endDate,10))
        ls.append(gain(x, endDate,20))
        ls.append(gain(x, endDate,30))
        ls.append(gain(x, endDate,60))
        ls.append(gain(x, endDate,90))
        ls.append(gain(x, endDate,120))
        ls.append(gain(x, endDate,180))
        ls.append(gain(x, endDate,240))
        ls.append(gain(x, endDate,300))
        ls.append(gain(x, endDate,360))

        lsStockGains.append(ls)

    with open('csv-files/multDayTests.csv', 'wb') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

        lsTopStr = ",".join(str(x) for x in lsTop)
        print lsTopStr
        mywriter.writerow([lsTopStr])
        str1 = "Date:{}".format(endDate)
        mywriter.writerow([str1])

        for ls in lsStockGains:
        	xStr = ",".join(str(x) for x in ls)
        	mywriter.writerow([xStr])


       	lsSuccessRate = ["Success Rate"]
       	len1 = len(lsStockGains[0])
       	#print len1 #should be 2 for the test

       	for i in range(1, len1):
       		effective = 0
       		for s in lsStockGains:
       			if (s[i] > 0):
       				effective = effective + 1


       		succRate = float(effective)/len(lsStockGains)
       		lsSuccessRate.append(succRate)

       	succStr = ",".join(str(x) for x in lsSuccessRate)
        mywriter.writerow([succStr])


#an.sp500CSVCare("2015-01-22", "2016-01-22",65)
stocks =  an.readOwnCSV()
#stocks = ["GOOGL", "CSCO"]
#dayGains(stocks, "2017-03-22", 5)
multDaysTests(stocks, "2016-01-22")

