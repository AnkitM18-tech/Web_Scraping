from __future__ import unicode_literals
import json
import requests
import pandas as pd

from flask import Flask,request,render_template,Response,session,redirect,url_for
app=Flask(__name__)

@app.route("/")
def scrape():
    params={
        "spider_name":"thespider",          #go to the spider
        "start_requests":True,              #Start urls requests.
    }
    response=requests.get("http://localhost:9080/crawl.json",params)
    data=json.loads(response.text)
    df=pd.DataFrame(data=data["items"],columns=["Title","Price","Stock","Star"])
    return render_template("simple.html",tables=[df.to_html(classes="data",index=False)],titles=df.columns.values)

if __name__=="__main__":
    app.run(debug=True,port=1234)

#put the app folder inside the project/bot folder(TheSpider) where all other scripts are present.