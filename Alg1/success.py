

import matplotlib.pyplot as plt
import numpy as np
import csv

import data_helper as dh
import aroon as an

from datetime import datetime, timedelta




def fiveDayGain(stocks, endDate):

    effective = 0
    for x in stocks:
        ret = dh.get_historical_data(endDate, subtractDays(endDate, -5), x)
        prices = ret[1]
        diff = prices[len(prices)-1] - prices[0]

        print "{}: {}".format(x, diff)
        if diff > 0:
            effective = effective + 1
        
    succRate = float(effective)/len(stocks)
    print "The success rate is : " + str(succRate)

def subtractDays(dateStr, daysR):

    start = datetime.strptime(dateStr, "%Y-%m-%d")
    newDate = start - timedelta(days=daysR)
    newDateStr = str(newDate.date())
    return newDateStr

#an.sp500CSVCare("2016-03-22", "2017-03-22",65)
stocks =  an.readOwnCSV()
fiveDayGain(stocks, "2017-03-22")
