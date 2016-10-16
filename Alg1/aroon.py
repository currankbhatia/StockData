import matplotlib.pyplot as plt

import numpy as np
from sp500 import get_historical_data, print_historical_data, plot_data, data_list, plot_data_xy
from sp500 import data_lists_reversed


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
    #plt.plot_date(dataRev[2], aroonList[1],  '-')
    list1 = [50 for i in range(len(dataRev[2]))]
    plt.plot_date(dataRev[2], list1, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()

startTime = "2005-01-01"
endTime = "2006-01-01" 

data = get_historical_data(startTime, endTime, 'AAPL')

plot_aroon(data)


