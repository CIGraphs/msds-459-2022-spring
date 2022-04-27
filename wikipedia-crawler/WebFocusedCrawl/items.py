# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WebfocusedcrawlItem(scrapy.Item):
    # define the fields for item jsontext:
    # name = scrapy.Field()
    keywords = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field() 
    text = scrapy.Field()

