import urllib2
from yahoo_finance import Share
import numpy

def getYearData(symbol, start, end):

	yahoo = Share(symbol)
	x = yahoo.get_historical(start, end)

	arr = list() #list of dicts
	for i in range(0, len(x)):
		
		tel = {'id': i, 'closing_price': x[i]['Adj_Close'], 'date': x[i]['Date']}
		arr.append(tel)

	

	for j in range(0, len(x)):
		dict1 =  arr[j]
		#print dict1['closing_price']


	return arr


def correlation(dict1, dict2, day_st, day_end):
	
	
	#why is i backwards?
	
	dict1Vector = list()
	for i in range(day_st, day_end):
		dict1Vector.append(dict1[i]['closing_price'])


	dict2Vector = list()
	for i in range(day_st, day_end):
		dict2Vector.append(dict2[i]['closing_price'])
	

	aVar =  numpy.corrcoef(dict1Vector,dict2Vector)
	
	return aVar[0][1]


def correlationIntervals(dict1, dict2, maxNum, interval):


	print ("Running intervals of %d", (interval))

	retList = list()

	i = 0
	while (i < maxNum):	
		i+=interval
		if (i > maxNum):
			i = maxNum
		
		#print ("i is %d" % (i))	 
	 	#print correlation(dict1, dict2, i-interval, i)
		tel = {'start': i-interval, 'end': i, 'corr': correlation(dict1, dict2, i-interval, i)}
		retList.append(tel)	


	i = interval/2
	while (i < maxNum):	
		i+=interval
		if (i > maxNum):
			i = maxNum
		
		#print ("i is %d" % (i))	 
	 	#print correlation(dict1, dict2, i-interval, i)
		tel = {'start': i-interval, 'end': i, 'corr': correlation(dict1, dict2, i-interval, i)}
		retList.append(tel)	


	return retList

def correlationTests(dict1, dict2):

	retList = list()

	y = correlationIntervals(dict1, dict2, len(dict1), len(dict1)/10)
	for x in range(0, len(y)):
		retList.append(y[x])

	y = correlationIntervals(dict1, dict2, len(dict1), len(dict1)/5)
	for x in range(0, len(y)):
		retList.append(y[x])

	y = correlationIntervals(dict1, dict2, len(dict1), len(dict1)/3)
	for x in range(0, len(y)):
		retList.append(y[x])

	y = correlationIntervals(dict1, dict2, len(dict1), len(dict1))
	for x in range(0, len(y)):
		
		print x
		retList.append(y[x])
	
	return retList



#def sigData(dict1, dict2):




startTime = "2015-05-05"
endTime = "2016-05-05"	

gold = getYearData('GDX', startTime, endTime)
 
apple = getYearData('^GSPC', startTime, endTime)

#correlation(gold, apple, 0, len(gold))

#correlationIntervals(gold, apple, len(gold), 20)

print correlationTests(gold, apple)
print "--------------------------------------"


#print goldVector
#print appleVector


