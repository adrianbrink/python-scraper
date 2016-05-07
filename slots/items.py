# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SlotsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    software = scrapy.Field()
    slot_reels = scrapy.Field()
    volatility = scrapy.Field()
    coins_range = scrapy.Field()
    jackpot = scrapy.Field()
    bonus = scrapy.Field()
    pass
