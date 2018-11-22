# -*- coding: utf-8 -*-
import scrapy
from base64 import *
import re

class JiandanmeiziSpider(scrapy.Spider):
    name = 'jiandanmeizi'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):
        hash_list = response.xpath("//span[@class ='img-hash']/text()").extract()
        for hash in hash_list:
            item = {}
            print(hash)
            m = hash.encode('utf-8')
            m = b64decode(m)
            item["pic"] = "http:"+str(m, 'utf-8')
            item["pic"] = item["pic"].replace('mw600','large')
            yield item
        next_url = response.xpath("//a[@title ='Older Comments']/@href").extract_first()
        next_url = "http:" + next_url
        # next_url.replace('mw600','large')
        print(next_url)
        if next_url is not None:
            yield scrapy.Request(next_url,callback=self.parse)