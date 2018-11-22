# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        # for pic in item["pics"]:
            # item["pic"] = pic
        yield scrapy.Request(url=item["pic"])

    def file_path(self, request, response=None, info=None):
        image_name = request.url.split('http://')[-1]
        image_name = image_name.replace("/","-")
        return './jiandan/%s'%(image_name)

