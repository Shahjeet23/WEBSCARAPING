import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.theguardian.com/football/premierleague/table"
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
table=soup.find("table",class_="table table--football table--league-table table--responsive-font table--striped")
headers=table.find_all("th")
# print(headers)
titles=[]
for i in headers:
    title=i.text
    titles.append(title)
titles=titles[1:-1]
df = pd.DataFrame(columns=titles)
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    
    l = len(df)
    df.loc[l] = row[1:-1]
print(df)
# duprows=[tr.text for tr in table.find_all('td')]
# print(duprows)S
df.to_csv("football.csv")
# print(df[:,1])