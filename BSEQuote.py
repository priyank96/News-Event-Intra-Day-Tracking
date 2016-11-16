"""stock price data from google finance"""

import urllib.request as  urllib2
from bs4 import BeautifulSoup as bs
from datetime import datetime, time
import csv


def static(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func

    return decorate


def toFloat(result):
    val = []
    for i in result:
        if i == '+' or i == '-' or i.isnumeric() or i == '.':
            val.append(i)
    val = ''.join(val)
    return float(val)


@static("line_counter", 0)
def getPrice(symbol, mode='real'):
    if mode == 'simulated':
        with open('TradeLog.csv', 'r') as fil:
            for i, line in enumerate(fil):
                if i == getPrice.line_counter:
                    return line.split(',')

    url = "https://www.google.com/finance?q=BOM%3A" + symbol
    val = []
    while len(val) != 3:
        try:
            r = urllib2.urlopen(url)
            content = r.read()
        except urllib2.HTTPError as e:
            content = e.read()

        soup = bs(content, "html.parser")
        val = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        result = soup.find("span", {"class": "pr"})
        if result is not None:
            val.append(toFloat(result.contents[1].string))

            result = soup.find("span", {"class": "ch bld"})
            val.append(toFloat(result.contents[2].string))

    return val  # time,price, change


if __name__ == '__main__':
    print(getPrice('524804'))
