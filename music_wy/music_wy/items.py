# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicWyItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field

    # music
    '''
    name = scrapy.Field()
    hits = scrapy.Field()
    content = scrapy.Field()
    # '''

    # spider
    #'''
    ip = scrapy.Field()  # ip地址
    port = scrapy.Field()  # 端口号
    delay = scrapy.Field()  # 延迟
    deadline = scrapy.Field()
    # '''
    # pass
