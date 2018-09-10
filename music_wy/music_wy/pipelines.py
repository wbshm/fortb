# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from bson import ObjectId


class MusicWyPipeline(object):
    myClient: None
    myDb: None
    mySets: None

    def process_item(self, item, spider):
        """
        需要传入的参数为：

        item (Item 对象) ： 被爬取的 item
        spider (Spider 对象) ：
        该方法会被每一个 item pipeline 组件所调用，process_item 必须返回以下其中的任意一个对象：

        一个 dict
        一个 Item 对象或者它的子类对象
        一个 Twisted Deferred 对象
        一个 DropItem exception；如果返回此异常，则该 item 将不会被后续的 item pipeline 所继续访问
        注意：该方法是Item Pipeline必须实现的方法，其它三个方法（open_spider/close_spider/from_crawler）是可选的方法

        :param item: 被爬取的 item
        :param spider: 爬取该 item 的 spider
        :return:
        """
        item['_id'] = ObjectId()
        self.mySets.insert_one(item)
        return item

    def open_spider(self, spider):
        self.myClient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.myDb = self.myClient['fortb']  # 数据库
        self.mySets = self.myDb['music_wy']
        pass

    def close_spider(self, spider):
        self.myClient.close()
        self.myClient = None
        pass
