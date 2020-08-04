# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import csv 
import  logging

class CrawlPipeline:
    def __init__(self):
        self.file = open('files.csv','a+')
        #self.bloomFilter = rBloomFilter.rBloomFilter(100000, 0.01, 'bing')
    def process_item(self, item, spider):
        self.file = open('files.csv','a+', newline='')
        items=[]
        items.append(item)
        keys = items[0].keys()
        dict_writer=csv.DictWriter(self.file, keys)
        with self.file:
            dict_writer.writerows(items)
        return item
