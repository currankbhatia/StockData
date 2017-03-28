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

    #dataLists = data_lists_reversed(data)
    #dataLs = dataLists[0]


    priceLs = data[1]
    datesLs = data[0] 
    

    aroonList = [0 for i in range(len(priceLs))] #[None]*(len(dataLs))
    aroonList2 = [0 for i in range(len(priceLs))] #[None]*(len(dataLs))
    #print aroonList
    for i in range(25,len(datesLs)):
        #print i
        #print datesLs[i]
        list25 = priceLs[i-25:i]
        aroonList[i] = aroon_up_oneday(list25)
        aroonList2[i] = aroon_down_oneday(list25)

    return [aroonList, aroonList2]


def plot_aroon(data):

    

    aroonList = make_aroon_list(data)

    #dataRev = data_lists_reversed(data)
    
    #print dataRev[2]
    plt.figure(1)
    plt.subplot(211)
    plt.plot_date(data[0], data[1], '-')
    plt.gcf().autofmt_xdate(rotation=45)

    plt.subplot(212)
    plt.plot_date(data[0], aroonList[0],  '-')
    plt.plot_date(data[0], aroonList[1],  '-')
    list1 = [50 for i in range(len(data[0]))]
    plt.plot_date(data[0], list1, '-')
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()


def plot_company(startTime, endTime, company):
    #Year-Month-Day

    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    
    #print len(aroon_data)
    #print len(aroon_data[0])
    #print aroon_data 
    plot_aroon(data)

    return aroon_data;

def isTrending(numAbove, aroon_data, company):
    """
        numAbove: essentially strengh of trend
        daysPositve: number of days that the aroonIndicator is above numAbove
    
        Checks if in reached above the numAbove in 6 out of the last 10 days
   
    """

    #print aroon_data 

    days = 10
    daysPositive = 6

    up_data = aroon_data[0]
    count = 0
    
    for i in range(len(up_data)-1, len(up_data)-days-1, -1):
        #print up_data[i]
        #print i
        if up_data[i] >= numAbove:
           count = count + 1
            
    if count < daysPositive: 
        print company + " : Not trending"
        return False
        
    print company + " : Is Trending"
    return True


def checkCompanyPositive(startTime, endTime, company, numAbove):
   
    #print company + " is the company"
    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    
    return isTrending( numAbove, aroon_data, company)

def crossoverPositive(daysLast, aroon_data, company):

    #check if data is large enough for daysLast
    if len(aroon_data[0]) < daysLast:
        print "Error for crossover Positive"
        return False
    
    len1 = len(aroon_data[0])

    bool1 = True
    #if aroon down is higher than aroon up then bool1 is false
    if (aroon_data[0][len1-daysLast-1] < aroon_data[1][len1-daysLast-1]):
        bool1 = False

    for i in range( len1-1, len1-daysLast-1, -1):
        #if bool1 is false, and aroon up is greater than aroon down, then it switched and we
        # have crossover
        if ((not bool1) and (aroon_data[0][i] > aroon_data[1][i])):
            return True



    return False
        


def crossoverNegative(daysLast, aroon_data, company):

    #check if data is large enough for daysLast
    if len(aroon_data[0]) < daysLast:
        print "Error for crossover Positive"
        return False
    
    len1 = len(aroon_data[0])

    bool1 = True
    #if aroon down is higher than aroon up then bool1 is false
    if (aroon_data[0][len1-daysLast-1] > aroon_data[1][len1-daysLast-1]):
        bool1 = False

    for i in range( len1-1, len1-daysLast-1, -1):
        #if bool1 is false, and aroon up is greater than aroon down, then it switched and we
        # have crossover
        if ((not bool1) and (aroon_data[0][i] < aroon_data[1][i])):
            return True

    return False


def checkCrossoverPositive(startTime, endTime, company, numAbove):

    """
        Checks if has met crossover mark and has stock heading in uptrend
        daysLast: Checks for last 20 days for the crossover mark, if it exists
    """

    #print company + " is the company"
    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    daysLast = 20
    boolCross = crossoverPositive(daysLast, aroon_data,company)
    if boolCross:
        #print company + " has had a positive crossover"
        return True
    else:
        #print company + " did not have a positive crossover"
        return False

def checkCrossoverNegative(startTime, endTime, company, numAbove):

    """
        Checks if has met crossover mark and has stock heading in uptrend
        daysLast: Checks for last 20 days for the crossover mark, if it exists
    """

    #print company + " is the company"
    data = get_historical_data(startTime, endTime, company)
    
    aroon_data = make_aroon_list(data)
    daysLast = 20
    boolCross = crossoverNegative(daysLast, aroon_data,company)
    if boolCross:
        #print company + " has had a negative crossover"
        return True
    else:
        #print company + " did not have a negative crossover"
        return False


def checkSP500Positive(startTime, endTime, numAbove):

    with open('../Summer/constituents.csv') as file:
        read = csv.DictReader(file)
        sp500List = list()
        trendList = list()



        for row in read: 
            #print ','.join(row)
            #print row['Symbol']
            sp500List.append(row['Symbol'])
            #print type(row['Symbol'])
        
        i = 0
        for x in sp500List:
            i = i + 1
            if (i == 5):
                break;
            print "Company: {}".format(x)
            twoList = []
            twoList.append(x)
            #y = checkCompanyPositive(startTime, endTime, x, numAbove)
            data = get_historical_data(startTime, endTime, x) 
            aroon_data = make_aroon_list(data)
            
            y = isTrending( numAbove, aroon_data, x)
            daysLast = 20
            crossPos = crossoverPositive(daysLast, aroon_data,x) 
            crossNeg = crossoverNegative(daysLast, aroon_data,x)
            twoList.append(y)
            #crossPos = checkCrossoverPositive(startTime, endTime, x, numAbove)
            #crossNeg = checkCrossoverNegative(startTime, endTime, x, numAbove)
            twoList.append(crossPos)
            twoList.append(crossNeg)
            trendList.append(twoList)
            print "Trending: {}, CrossPos: {}, CrossNeg: {}".format(y, crossPos, crossNeg)

    return trendList

def sp500CSV(startTime, endTime, numAbove):
    
    print "running..."
    
    printList = checkSP500Positive(startTime, endTime, numAbove)

    with open('sp500aroontrends.csv', 'wb') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        str1 = "StartTime:{},EndTime:{},numAbove:{}".format(startTime, endTime, numAbove)

        mywriter.writerow(["Company,ifTrending,CrossoverPositive,CrossoverNegative"])
        
        mywriter.writerow([str1])

        for x in printList:
            mywriter.writerow(["{},{},{},{}".format(x[0], x[1],x[2],x[3])])

def sp500CSVCare(startTime, endTime, numAbove):


    with open('sp500aroontrendscare.csv', 'wb') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        str1 = "StartTime:{},EndTime:{},numAbove:{}".format(startTime, endTime, numAbove)

        mywriter.writerow(["Company,ifTrending,CrossoverPositive,CrossoverNegative"])
        
        mywriter.writerow([str1])


        with open('../Summer/constituents.csv') as file:
            read = csv.DictReader(file)
            sp500List = list()
            trendList = list()

            for row in read: 
                #print ','.join(row)
                #print row['Symbol']
                sp500List.append(row['Symbol'])
                #print type(row['Symbol'])
            
            #i = 0
            for x in sp500List:
                #i = i + 1
                #if (i == 5):
                    #break;
                print "Company: {}".format(x)
                twoList = []
                twoList.append(x)
                #y = checkCompanyPositive(startTime, endTime, x, numAbove)
                data = get_historical_data(startTime, endTime, x) 
                aroon_data = make_aroon_list(data)
                
                y = isTrending( numAbove, aroon_data, x)
                daysLast = 20
                crossPos = crossoverPositive(daysLast, aroon_data,x) 
                crossNeg = crossoverNegative(daysLast, aroon_data,x)
                twoList.append(y)
                #crossPos = checkCrossoverPositive(startTime, endTime, x, numAbove)
                #crossNeg = checkCrossoverNegative(startTime, endTime, x, numAbove)
                twoList.append(crossPos)
                twoList.append(crossNeg)
                trendList.append(twoList)
                print "Trending: {}, CrossPos: {}, CrossNeg: {}".format(y, crossPos, crossNeg)
                # remember x is company, y is isTrending
                mywriter.writerow(["{},{},{},{}".format(x, y, crossPos,crossNeg)])



def readOwnCSV():
    with open('sp500aroontrendscare.csv') as file2:
        read2 = csv.DictReader(file2)

        #i = 0
        list1 = []
        for row in read2: 
            #print row
            if row['ifTrending'] == 'True' and row['CrossoverPositive'] == 'True':
                #print row['Company'] 
                list1.append(row['Company'])

    return list1

#sp500CSVCare("2016-03-27", "2017-03-27",65)
#readOwnCSV()

#checkSP500Positive("2016-01-01", "2017-02-26",65)
#checkCompanyPositive("2016-01-01", "2017-02-26", "ABT", 65)
#print get_historical_data("2016-01-01", "2017-02-26", "ABT")
#plot_company("2016-03-02", "2017-03-02", 'ABT')

#checkCrossoverNegative("2016-01-01", "2016-11-01", "YHOO", 65)
#checkCrossoverPositive("2016-01-01", "2016-11-01", "YHOO", 65)
#plot_company("2016-01-01", "2016-11-01", "YHOO")

#plot_company("2016-03-27", "2017-03-27", 'GOOGL')


#startTime = "2015-01-01"
#endTime = "2016-01-01" 
#data = get_historical_data(startTime, endTime, 'TSLA')
#print data
#dataLists = data_lists_reversed(data)
#priceLs = dataLists[1]
#datesLs = dataLists[2] 

#aroon = make_aroon_list(data)[0]

#print_lists([priceLs, aroon, datesLs ])


#plot_aroon(data)

