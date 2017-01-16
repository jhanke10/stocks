from urllib2 import *

#Gets the .csv file for the particular stock from Quandl API
def getStock(company, key):
	url = "https://www.quandl.com/api/v3/datasets/WIKI/" + company.upper() + ".csv?api_key=" + key
	try:
		stock = urlopen(url).read().split("\n")

		#Get the header for each of the numbers
		header = stock[0].split(",")[1:6]
		return stock[1:len(stock)-1], header
	except URLError, e:
		print "Error: ", e
		return None

#Parse the information into a dict format for easy access
def parseFile(files, headers):
	stocks = {}

	#Go through list and set up dictionary
	for info in files:
		info = info.split(",")
		day = {}
		for i in range(len(headers)):
			day[headers[i]] = info[i+1]
		stocks[info[0]] = day

	return stocks

def main():
	#Gets the data for the stock
	company = raw_input("What company do you want the stock price of? ")
	stocks, header = getStock(company, "Insert Key Here")
	stock = parseFile(stocks, header)

	#Access the information from the data


if __name__ == "__main__":main()