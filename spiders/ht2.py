# -*- coding: utf-8 -*-
import scrapy


class Ht2Spider(scrapy.Spider):
    name = 'ht2'
    allowed_domains = ['959ii.com']
    start_urls = ['https://www.959ii.com/meinv/index.html']

    def parse(self, response):
        li_list = response.xpath("//div[@id='tpl-img-content']/li")
        for li in li_list:
            yield scrapy.Request("https://www.959ii.com"+li.xpath(".//a/@href").extract_first(),callback=self.parse_next)

    def parse_next(self,response):
        lilis = response.xpath("//div[@id='tpl-img-content']/li")
        for lili in lilis:
            url = lili.xpath("./a/@href").extract_first()
            url = "https://www.959ii.com"+url
            yield scrapy.Request(url,callback=self.parse_next_2)
            print (url)

        next_url = response.xpath("./a[contains(text(),'下一页')]/@href").extract_first()
        if next_url is not None:
            next_url = "https://www.959ii.com"+next_url
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse_next)

    def parse_next_2(self,response):
        item = {}
        pics = response.xpath("//div[@class='content']/img/@data-original").extract()
        print(pics)
        for pic in pics:
            item["pic"] = pic
            print (pic)
            yield item


    # def parse_details(self,response):
    #     pass