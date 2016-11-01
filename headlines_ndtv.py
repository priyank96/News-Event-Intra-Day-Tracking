'''headlines from first three pages of latest section on profit.ndtv, intended for non-commercial, personal use'''
from bs4 import BeautifulSoup
import urllib.request
import dateutil.parser as dparser
from datetime import time
page_no=1
url="http://profit.ndtv.com/news/latest/page-"
f=open("headlines(ndtv).txt",'w')

while(page_no!=4):
    page=urllib.request.urlopen(url+str(page_no))
    soup=BeautifulSoup(page.read(),"html.parser")
    anchors = [div.find('a') for div in soup.findAll('div', {'class': 'nstory_header'})]
    times =  [div for div in soup.findAll('div', {'class': 'nstory_dateline'})]
    for i in range(0,len(anchors)):
        #print(anchors[i].text)
        f.write(anchors[i].text.lstrip()+'\n')
        publish_time = dparser.parse(times[i].text,fuzzy=True)
        if  publish_time.time()< time(16,0):
            break
        print(publish_time)
    page_no+=1
f.write("End")
f.close()

print("Done- profit.ndtv")

     
