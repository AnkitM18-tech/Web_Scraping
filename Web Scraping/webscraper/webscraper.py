from flask import Flask,render_template
app=Flask(__name__)
from bs4 import BeautifulSoup
import requests

url="https://www.worldometers.info/coronavirus/"
req=requests.get(url)
bsObj=BeautifulSoup(req.text,"html.parser")

data=bsObj.find_all("div",class_="maincounter-number")           #every instances of counter(Total,Deaths,recovered)
total_cases=int(data[0].text.strip().replace(",",""))
recovered=int(data[2].text.strip().replace(",",""))
deaths=int(data[1].text.strip().replace(",",""))
active_cases=total_cases-(recovered+deaths)
percentage_recovered=round((recovered/total_cases)*100,2)
percentage_death=round((deaths/total_cases)*100,2)

@app.route("/")

def home():
    return render_template("home.html",total_cases=total_cases,recovered=recovered,deaths=deaths,
    active_cases=active_cases,percentage_recovered=percentage_recovered,percentage_death=percentage_death)



if __name__ =="__main__":
    app.run(debug=True)