import json

import scrapy
from scrapy import Request


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED']
    start_urls = ['https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED']
    seasons = []

    def parse(self, response):
        yield Request(url='https://www1.gowatchseries.bz/search.html?keyword=DISAPPEARED',
                      callback=self.extract_season, dont_filter=True)

    def extract_season(self, response):

        for i in response.xpath('//*[@id="left"]/div[3]/ul/li'):
            link_season = i.xpath('a/@href').extract_first()
            season_name = i.xpath('a/div[3]/text()').extract_first()

            if link_season:
                link_season = response.urljoin(link_season)
                yield scrapy.Request(url=link_season, callback=self.extract_episode, dont_filter=True)

        nex_page = response.xpath('//*[@id="left"]/div[5]/nav/ul/li[3]/a/@href').extract_first()
        if nex_page:
            link_nex_page = response.urljoin(nex_page)
            if str(link_nex_page) != str(response.url):
                yield scrapy.Request(url=link_nex_page, callback=self.extract_season, dont_filter=True)
        else:
            with open("movies.json", "w", encoding="UTF-8") as json_file:
                json.dump(self.seasons, json_file, indent=4)

    def extract_episode(self, response):
        list_episodes = []
        for i in response.xpath('//*[@id="left"]/div/div[3]/div[1]/div[3]/ul/li'):
            episode_name = i.xpath('a/text()').extract_first()
            link_episode = i.xpath('a/@href').extract_first()
            link_episode = response.urljoin(link_episode)
            item = {
                "episode_name": str(episode_name).strip(),
                "link_episode": link_episode
            }
            list_episodes.append(item)

        season = {
            "link_season": response.url,
            "episodes": list_episodes
        }
        self.seasons.append(season)

        # loader = ItemLoader(item=ScrapyMoviesItem(), response=response)
        # loader.add_value('link_season', response.url)
        # loader.add_value('episodes', list_episodes)
        #
        # yield loader.load_item()
