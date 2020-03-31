# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from firebase import firebase


class covid19Pipeline(object):
    url = "https://cov19updates-b9843.firebaseio.com/"

    def __init__(self):
        self.FBConn = firebase.FirebaseApplication(self.url, None)

    def process_item(self, item, spider):
        self.store_data(item)
        return item

    def store_data(self, item):
        self.FBConn.put("/", item['country'], dict(item))
