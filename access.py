
import urllib2
from yahoo_finance import Share


# Good info on the Yahoo API : http://www.jarloo.com/yahoo_finance/
# Used this helper to get information easier https://pypi.python.org/pypi/yahoo-finance



def printList(list1):

	for i in range(0, len(list1)):
		print list1[i]
		print "close is: {}".format(list1[i]['Adj_Close'])
		



def testAPIHelper():
	yahoo = Share('^GSPC')
	print yahoo.get_price()	
	one  = yahoo.get_historical("2000-01-02", "2000-01-04")
	printList(one)



def getDataDirectly():
	response = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+MSFT&f=nab')
	html = response.read()
	print html

testAPIHelper()
#getDataDirectly()
