# crawl data
crawler website by scrapy in python

Environment: python 3.7

## Fake IP by VPN to US - Los Angeles


## create project scrapy
scrapy startproject scrapy_movies

scrapy genspider movies https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

scrapy shell https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

## Start crawl data
scrapy crawl movies
