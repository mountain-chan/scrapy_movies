# crawl data
crawler website by scrapy in python

Environment: python 3.7

## Update Proxy list
Step1: get file list-proxy on https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt to update proxy list

Step2: run file update_us_proxy.py to get only us proxy 


## create project scrapy
scrapy startproject scrapy_movies

scrapy genspider movies https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

scrapy shell https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED

## Start crawl data
scrapy crawl movies
