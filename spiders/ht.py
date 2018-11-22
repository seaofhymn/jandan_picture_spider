# -*- coding: utf-8 -*-
import scrapy


class HtSpider(scrapy.Spider):
    name = 'ht'
    allowed_domains = ['599ii.com']
    start_urls = ['https://www.599ii.com/tupian/list-%E6%B8%85%E7%BA%AF%E5%94%AF%E7%BE%8E.html']

    def parse(self, response):
        url_tmp = response.xpath("//div[@id='tpl-img-content']//li//a/@href").extract()
        url_next = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        for url in url_tmp:
            url = "https://www.599ii.com"+url
            print(url)
            yield scrapy.Request(url,callback=self.parse_next)
        print(url_next)
        if url_next is not None:
            url_next = "https://www.599ii.com/"+url_next
        yield scrapy.Request(url_next,callback=self.parse)
    def parse_next(self,response):
        item = {}
        pics = response.xpath("//img[@class='videopic lazy']/@data-original").extract()
        # print(pics)
        for pic in pics:
            print(pic)
            item["pic"] = pic
            # yield scrapy.Request(pic,callback=self.parse_con)
            yield item
    # def parse_con(self,response):
    #     item = {}
    #     item["content"] = response




