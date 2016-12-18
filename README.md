# WebCrawler
Python , Scrapy ,MongoDB , crawler , Web Mining

Example of Web Crawler to get data from the Web with Python Scrapy and MongoDB .

You have access to several sites: http://www.placesonline.com/ & http://www.tripadvisor.com/.
The goal is to list all of them and extract the relevant information (title, url, rate). 
This is where Scrapy enters into action

Installation:
- Python 2.7
- Scrapy 1.1.1 [conda install -c anaconda scrapy=1.1.1] or [pip install scrapy==1.1.1]
- PyMongo for storing the data in MongoDB. [pip install pymongo]
- You need to install MongoDB as well

Let’s start a new Scrapy project:
[scrapy startproject webcrawler]

Specify Data:
The items.py file is used to define storage “containers” for the data that we plan to scrape. add some items that we actually want to collect.

Run the following command within the “WebCrawler” directory widh the output to a JSON file:
[scrapy crawl stack -o items.json -t json]
[scrapy crawl finder -o items.json -t json]

Or just the following command and the Data will be Stored  in MongoDB:
[scrapy crawl stack]
