"""stock price data from google finance"""

import urllib.request as  urllib2
import urllib
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import sleep



def static(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func

    return decorate


def to_float(result):
    val = []
    for i in result:
        if i == '+' or i == '-' or i.isnumeric() or i == '.':
            val.append(i)
    val = ''.join(val)
    return float(val)


@static("line_counter", 0)
def get_price(symbol):
    url = "https://www.google.com/finance?q=BOM%3A" + symbol
    val = []
    while len(val) != 3:
        while True:
            try:
                r = urllib2.urlopen(url)
                content = r.read()
                break
            except urllib2.HTTPError as e:
                content = e.read()
                break
            except urllib.error.URLError:
                sleep(2) #wait two seconds and try again
                pass


        soup = bs(content, "html.parser")
        val = [datetime.now().strftime("%H:%M:%S")]

        result = soup.find("span", {"class": "pr"})
        if result is not None:
            val.append(to_float(result.contents[1].string))

            result = soup.find("span", {"class": "ch bld"})
            val.append(to_float(result.contents[2].string))

    return val  # time,price, change


if __name__ == '__main__':
    print(get_price('524804'))
