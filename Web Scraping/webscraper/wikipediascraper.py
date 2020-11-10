from flask import Flask,render_template
app=Flask(__name__)
from bs4 import BeautifulSoup
import requests

url="https://en.m.wikipedia.org/wiki/List_of_largest_Internet_companies"
req=requests.get(url)
bsObj=BeautifulSoup(req.text,"html.parser")
data=bsObj.find("table",{"class":"wikitable sortable mw-collapsible"})

table_data=[]
trs=bsObj.select("tr")

for tr in trs[1:10]:                   #first column has header,so it's empty.We start from 1 instead.
    row=[]
    for t in tr.select("td")[:3]:
        row.extend([t.text.strip()])
    table_data.append(row)

req_data=table_data


@app.route("/")

def home():
    return render_template("homewiki.html",req_data=req_data)

if __name__=="__main__":
    app.run(debug=True)