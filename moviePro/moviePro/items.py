# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class DetailItem(scrapy.Item):
    name = scrapy.Field()
    spaker = scrapy.Field()
