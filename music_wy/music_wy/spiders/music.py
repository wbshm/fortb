# -*- coding: utf-8 -*-
import scrapy


# https://music.163.com/#/playlist?id=924680166
class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):  # 默认解析器方法
        print('i am in parse')
