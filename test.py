import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://money.rediff.com/gainers/nse/daily/nifty').text
soup = BeautifulSoup(website_url,'lxml')
My_table = soup.find('table',{'class':'dataTable'})
links = My_table.findAll('a')
stocks=[]
for link in links:
    a=link.text
    companya=a.replace("\n"," ").replace("\t"," ")
    company=companya.strip()
    stocks.append(company)
print(stocks)