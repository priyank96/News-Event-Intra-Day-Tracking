from bs4 import BeautifulSoup
import urllib.request
page_no=1
url="http://profit.ndtv.com/news/latest/page-"
f=open("headlines(ndtv).txt",'w')

while(page_no!=4):
    page=urllib.request.urlopen(url+str(page_no))
    soup=BeautifulSoup(page.read(),"html.parser")
    anchors = [div.find('a') for div in soup.findAll('div', {'class': 'nstory_header'})]
    for i in anchors:
        print(i.text)
        f.write(i.text.lstrip()+'\n') 
   
    page_no+=1
f.write("End")
f.close()

print("Done- profit.ndtv")

     
