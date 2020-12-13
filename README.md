# crawl data
crawler website by scrapy in python

Environment: python 3.7

## Update Proxy list
update proxy list in file us_proxy.txt


## create project scrapy
scrapy startproject scrapy_movies

scrapy genspider movies https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

scrapy shell https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

## Start crawl data
run main.py
