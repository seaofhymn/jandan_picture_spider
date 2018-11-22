# -*- coding: utf-8 -*-
import scrapy
import selenium
from selenium import webdriver
import requests
from lxml import etree
import random
import time
import scrapy
import urllib
import io
import sys
# from scrapy.http import Request,FormRequest

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/signin']
    # headers = {
    #     "User-Agent:": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

    # def start_requests(self):
    #     return [Request('https://www.zhihu.com/signin', headers=self.headers, meta={'cookiejar': 1},
    #                     callback=self.parse)]
    def getcookies(self):
        # con =response.xpath("//h2/text()").extract()
        dr = webdriver.Chrome()
        dr.get(self.start_urls[0])
        dr.find_element_by_name("username").send_keys("18047282835")
        dr.find_element_by_name("password").send_keys("172542qy")
        dr.find_element_by_class_name("SignFlow-submitButton").click()
        input =("qingshuru")
        time.sleep(20)
        cookie = dr.get_cookies()
        time.sleep(20)
        dr.close()
        print(cookie)

        return cookie

    def parse(self, response):
        yield scrapy.Request(url=self.start_urls[0], cookies = self.getcookies(), callback=self.after_login)

    def after_login(self,response):
        # sel = scrapy.Selector(response)
        print(response.body)
        yield response