import urllib2
from yahoo_finance import Share
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


startTime = "2015-05-05"
endTime = "2016-05-05" 

var1 = 'AAPL'
yahoo = Share(var1)
x = yahoo.get_historical(startTime, endTime)


# arr is a list of dictionaries with historical data
arr = list()
closingPrice = list()

for i in range(0, len(x)):
    tel = {'id': i, 'closing_price': x[i]['Adj_Close'], 'date': x[i]['Date']}
    #print x[i]['Adj_Close']
    arr.append(tel)
    closingPrice.append(tel['closing_price'])


for j in range(0, len(x)):
    dict1 = arr[j]
    print dict1['closing_price']



print closingPrice
print len(x)
#x1 = np.linspace(0, 365)
plt.plot(closingPrice) 
plt.show()