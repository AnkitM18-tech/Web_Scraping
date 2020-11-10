from __future__ import unicode_literals
import scrapy
pages=int(input('How many pages do you want to scrape? :'))
dictionary={"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(i+1) for i in range(pages)]

    def parse(self, response):
        #data={}
        books=response.css("ol.row")
        for book in books:
            for b in book.css("article.product_pod"):
                #data["title"]=b.css("a::attr(title)").getall()
                #data["price"]=b.css("div.product_price p.price_color::text").getall()
                #data["stock"]=b.css("div.product_price p.instock.availability::text").getall()[1].strip()
                #data["star"]=b.css("p::attr(class)").getall()[0].split()[-1]
                #data["star"]=[v for k,v in dictionary.items() if k in data["star"]][0]
                #yield data
                #scrapy crawl thespider -o ----.csv     to save the file
                #scrapy crawl thespiider   to run the crawler.
                #The above code gives redundancy in flask.so we are not using it.
                yield{
                    "Title": b.css("a::attr(title)").getall()[0],
                    "Price": b.css("div.product_price p.price_color::text").getall()[0],
                    "Stock": b.css("div.product_price p.instock.availability::text").getall()[1].strip(),
                    "Star": [v for k,v in dictionary.items() if k in b.css("p::attr(class)").getall()[0].split()[-1]][0]
                }

                #http://127.0.0.1:9080/crawl.json?spider_name=thespider&start_requests=true -scrapyrt page url.