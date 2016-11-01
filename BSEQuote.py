'''stock price data from google finance'''

import urllib.request as  urllib2
from bs4 import BeautifulSoup as bs
import sqlite3
from time import sleep
from datetime import datetime, time
import csv
import itertools

def toFloat(result):
    val=[]
    for i in result:
        if(i=='+' or i=='-' or i.isnumeric() or i=='.'):
            val.append(i)
    val = ''.join(val)
    return float(val)

def getPrice(ID):
    print("getting price")
    url = "https://www.google.com/finance?q=BOM%3A"+ID
    val=[]
    while len(val)!=3:
        try:
            r=urllib2.urlopen(url)
            content = r.read()
        except urllib2.HTTPError as e:
            content=e.read()
            
        
        soup = bs(content,"html.parser")
        val=[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    
    
        result = soup.find("span",{"class":"pr"})
        if result is not None:  
            val.append(toFloat(result.contents[1].string))

            result = soup.find("span",{"class":"ch bld"})
            val.append(toFloat(result.contents[2].string))
        
            

    return val #time,price, change

    
    
if __name__=='__main__':
    print(getPrice('524804'))
