import scrapy


class ScrapyMoviesItem(scrapy.Item):
    link_season = scrapy.Field()
    episodes = scrapy.Field()
