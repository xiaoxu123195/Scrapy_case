# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstbloodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    auto = scrapy.Field()
    another = scrapy.Field()
    times = scrapy.Field()
    fabulous = scrapy.Field()
    pass
