from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time

path="C:/Users/OCAC/Desktop/Web Scraping/SeleniumScraper/chromedriver"
chrome_options=Options()
chrome_options.add_argument("-incognito")
browser=webdriver.Chrome(path,options=chrome_options)
pages=3
url="http://books.toscrape.com/catalogue/page-1.html"

def get_data(start_url,pgs):
    current=0
    urls=browser.get(start_url)
    data={}
    df=pd.DataFrame(columns=["Title","Price","Stock","Star"])
    dict={"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    while current<pgs:
        books=browser.find_elements_by_css_selector("ol.row")
        for book in books:
            for b in book.find_elements_by_css_selector("article.product_pod"):
                data["Title"]=b.find_elements_by_css_selector("img")[0].get_attribute("alt")
                data["Price"]=b.find_elements_by_css_selector("div.product_price p.price_color")[0].text
                data["Stock"]=b.find_elements_by_css_selector("div.product_price p.instock.availability")[0].text
                data["Star"]=b.find_elements_by_css_selector("p")[0].get_attribute("class").split()[-1]
                data["Star"]=[v for k,v in dict.items() if k in data["Star"]][0]
                df=df.append(data,ignore_index=True)
        current+=1
        next=browser.find_elements_by_css_selector("li.next a")[0].click()
    return df

get_data(url,pages).to_excel("Selenium_Test.xlsx")