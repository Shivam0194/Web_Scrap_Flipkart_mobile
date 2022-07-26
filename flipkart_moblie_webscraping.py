# -*- coding: utf-8 -*-
"""Flipkart_Moblie_WebScraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tRxXUR_O1MNXTpuNcGNqHrNohH5IW_SK
"""

!pip install requests --quiet
!pip install beautifulsoup4 --upgrade --quiet

import requests
from bs4 import BeautifulSoup

ur='https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='

mobile_name=[]
mprice=[]
mrating=[]
speci=[]
for i in range(1,101):
  url=ur+str(i)
  response=requests.get(url)
  content=BeautifulSoup(response.content,'html.parser')
  name=content.find_all('div',{'class':'_4rR01T'})
  price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
  rating=content.find_all('div',{'class':'_3LWZlK'})
  spec=content.find_all('ul',{'class':'_1xgFaf'})
  

  for i in name:
    mobile_name.append(i.text)
  for i in price:
    mprice.append(i.text)
  for i in rating:
    mrating.append(i.text)
  for i in spec:
    speci.append(i.text)

mobile_dict={
    'Mobile Name':mobile_name,
    'Price':mprice,
    'Specification':speci
}

import pandas as pd

df=pd.DataFrame(mobile_dict)

df

df.to_csv('Mobile.csv',index=None)

