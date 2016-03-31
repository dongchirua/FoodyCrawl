# FoodyCrawl

A [Scrapy](http://scrapy.org/) application for scraping [Foody.vn](http://foody.vn)

Not well tested. Has probably lots of bugs. Just a demonstration how to use *InitSpider* for authentication in *foody.vn* 

That being said, it do work but you have to use at your own risk.

Installation
----------
	git clone  https://github.com/dongchirua/FoodyCrawl

Requirements
----------
	cd FoodyCrawl
	pip install -r requirements.txt

Run Spider
----------
	scrapy crawl food -a password=1234567890 -a user=user@somewhere.com

Advance
----------
You can use [MongoDB](https://www.mongodb.org/) to store scraped data. 

In `./Foody/setting.py`, you should provider appropriate configuration

	MONGODB_SERVER = "YOUR_HOST"
	MONGODB_PORT = 'PORT'
	MONGODB_DB = "DB_NAME"
	MONGODB_COLLECTION = "COLLECTION"

In `./Foody/piplines.py`, you have to 


- UNCOMMENT `def __init__`
- UNCOMMENT lines from **#23 to #34**
- COMMENT `return item` at line **#16**


----------
Please drop me an email if you want to discuss: *Hong QUY Nguyen (Mr), nguyen[dot]hquy[at]gmail[dot]com* where [dot] is '.' and [at] is '@'