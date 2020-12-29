import designed_mail
import csv
import requests
from bs4 import BeautifulSoup
l,m=[],0
URL1="https://www.flipkart.com/mi-notebook-14-core-i5-10th-gen-8-gb-512-gb-ssd-windows-10-home-jyu4243in-thin-light-laptop/p/itm970105b392f49"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "}
page1=requests.get(URL1,headers = headers)
soup1=BeautifulSoup(page1.content,"html.parser")
l.append(float((soup1.find("div", {"class":"_30jeq3 _16Jk6d"}).text.replace("₹","")).replace(",","")))
URL2="https://www.amazon.in/Notebook-i5-10210U-Windows-Graphics-XMA1901-FC/dp/B089F3WL8T"
page2=requests.get(URL2,headers = headers)
soup=BeautifulSoup(page2.content,"html.parser")
l.append(float(''.join(list((soup.find("span", {"id": "priceblock_ourprice"}).text))[2:]).replace(",","")))
with open("price.txt", "r") as name:
    v=float(name.read())

with open("price.txt", "w") as name:
    name.write(str(min(l)) if v>min(l) else str(v))
if v>min(l):
    print("Price drop detected Sending Mail")
    designed_mail.send("Flipkart" if l[0]==min(l) else "Amazon",str(min(l)),)
else:
    print("No Price Change")
    




