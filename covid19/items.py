# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class covid19Item(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()
    total_cases = scrapy.Field()
    new_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    new_deaths = scrapy.Field()
    total_recovered = scrapy.Field()
    active_cases = scrapy.Field()
    critical_cases = scrapy.Field()
    last_updated = scrapy.Field()
    pass
