"""headlines from first three pages of latest section on profit.ndtv, intended for non-commercial, personal use"""
from bs4 import BeautifulSoup
import urllib.request
import dateutil.parser as dparser
import datetime

page_no = 1
now = datetime.datetime.now()
if now.isoweekday() == 1:       # weekend checking
    cutoff = now - datetime.timedelta(days=3)
else:
    cutoff = now - datetime.timedelta(days=1
                                      )
cutoff = cutoff.replace(hour=16, minute=0)
print(cutoff)
url = "http://profit.ndtv.com/news/latest/page-"
f = open("headlines(ndtv).txt", 'w')

while page_no != 10:
    #print(page_no)
    page = urllib.request.urlopen(url+str(page_no))
    soup = BeautifulSoup(page.read(),"html.parser")
    #print(soup)
    anchors = [div.find('a') for div in soup.findAll('div', {'class': 'nstory_header'})]
    times = [div for div in soup.findAll('div', {'class': 'nstory_dateline'})]
    for i in range(0,len(anchors)):
        print(anchors[i].text)
        f.write(anchors[i].text.lstrip()+'\n')
        publish_time = dparser.parse(times[i].text, fuzzy=True)
        if publish_time < cutoff:
            print("here")
            break
    if i+1 != len(anchors):
        break
        
    page_no += 1
f.write("End")
f.close()

print("Done- profit.ndtv")

     
if __name__ == '__main__':
    with open("headlines(ndtv).txt", 'r') as f:
        print(f.read())
