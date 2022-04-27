# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from WebFocusedCrawl.items import WebfocusedcrawlItem  # item class 
from string import whitespace

class WebfocusedcrawlPipeline(object):
    def process_item(self, item, spider):
        item['text'] = [line for line in item['text'] if line not in whitespace]
        item['text'] = ''.join(item['text'])
        return item
