# Amazon_Scraper

Created a python script using Scrapy to scrap the data of Amazon by using product listing page. 
The names of the products are then scraped and inserted into an sqlite database. The prices of the products can also be extracted but there are some problems in the script due to which it is not able to scrap the prices of all the products. So the functionality to scrap the prices is not added right now.
The number of products that can be scraped can be increased by increasing the number of pages that are being queried in the search results by increasing the range of the for loop.
To run the script use the command:
# scrapy crawl amazon
