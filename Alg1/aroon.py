import matplotlib.pyplot as plt

import numpy as np
import csv
from data_helper import get_historical_data, print_historical_data, plot_data, data_list, plot_data_xy
from data_helper import data_lists_reversed, print_list, print_lists


def aroon_up_oneday(list25):
    flt = float(np.argmax(list25))
    val = (flt/25)*100
    return val


def aroon_down_oneday(list25):
    flt = float(np.argmin(list25))
    val = (flt/25)*100
    return val

def make_aroon_list(data):

    dataLists = data_lists_reversed(data)
    dataLs = dataLists[0]
    priceLs = dataLists[1]
    datesLs = dataLists[2] 
    
    aroonList = [0 for i in range(len(dataLs))] #[None]*(len(dataLs))
    aroonList2 = [0 for i in range(len(dataLs))] #[None]*(len(dataLs))
    #print aroonList
    for i in range(25,len(dataLs)):
        #print i
        #print datesLs[i]
        list25 = priceLs[i-25:i]
        aroonList[i] = aroon_up_oneday(list25)
        aroonList2[i] = aroon_down_oneday(list25)

    return [aroonList, aroonList2]


def plot_aroon(data):

    aroonList = make_aroon_list(data)

    dataRev = data_lists_reversed(data)
    plt.figure(1)
    plt.subplot(211)
    plt.plot_date(dataRev[2], dataRev[1], '-')
    plt.gcf().autofmt_xdate(rotation=45)

    plt.subplot(212)
    plt.plot_date(dataRev[2], aroonList[0],  '-')
    plt.plot_date(dataRev[2], aroonList[1],  '-')
    list1 = [50 for i in range(len(dataRev[2]))]
    plt.plot_date(dataRev[2], list1, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()


def plot_company(startTime, endTime, company):
    #Year-Month-Day

    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    
    #print aroon_data 
    
    plot_aroon(data)

    return aroon_data;

def isTrending(numAbove, aroon_data, company):
    """
        numAbove: essentially strengh of trend
        daysPositve: number of days that the aroonIndicator is above numAbove
    
        Checks if in reached above the numAbove in 6 out of the last 10 days
   
    """
    daysPositive = 10

    up_data = aroon_data[0]
    count = 0
    #for i in range(len(aroon_data)-1, len(aroon_data)-daysPositive, -1):
    for i in range(len(up_data)-1, len(up_data)-daysPositive-1, -1):
        #print up_data[i]
        if up_data[i] >= numAbove:
           count = count + 1
            
    if count < 6: 
        print company + " : Not trending"
        return False
        
    print company + " : Is Trending"
    return True


def checkCompanyPositive(startTime, endTime, company, numAbove):
   
    print company + " is the company"
    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    
    isTrending( numAbove, aroon_data, company)


def checkSP500Positive(startTime, endTime, numAbove):

    with open('../Summer/constituents.csv') as file:
        read = csv.DictReader(file)
        sp500List = list()
        
        for row in read: 
            #print ','.join(row)
            #print row['Symbol']
            sp500List.append(row['Symbol'])
            #print type(row['Symbol'])
        

        for x in sp500List:
            checkCompanyPositive(startTime, endTime, x, numAbove)


#checkSP500Positive("2016-01-01", "2017-02-09",65)
#checkCompanyPositive("2016-01-01", "2017-02-09", "TSLA", 65)



plot_company("2016-01-01", "2017-02-09", "TSLA")
#plot_company("2015-01-01", "2016-01-01", 'TSLA')


#startTime = "2015-01-01"
#endTime = "2016-01-01" 
#data = get_historical_data(startTime, endTime, 'TSLA')
#dataLists = data_lists_reversed(data)
#priceLs = dataLists[1]
#datesLs = dataLists[2] 

#aroon = make_aroon_list(data)[0]

#print_lists([priceLs, aroon, datesLs ])


#plot_aroon(data)


