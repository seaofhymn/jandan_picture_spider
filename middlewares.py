# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.text import TextResponse
from selenium.webdriver import ActionChains


# class ZhihuMiddleware(object):
#
#     # 处理请求函数
#     def process_request(self, request, spider):
#         # 声明一个Options对象
#         # opt = Options()
#         # 给对象添加一个--headless参数,表示无头启动
#         # opt.add_argument('--headless')
#         # 把配置参数应用到驱动创建的对象
#         dr = webdriver.Chrome()
#         # 打开requests中的地址
#         dr.get(request.url)
#
#         dr.find_element_by_name("username").send_keys("18047282835")
#         dr.find_element_by_name("password").send_keys("172542qy")
#         dr.find_element_by_class_name("Button SignFlow-submitButton Button--primary Button--blue").click()
#         # # 让浏览器滚动到底部
#         # for x in range(1, 11):
#         #     j = x / 10
#         #     js = "document.documentElement.scrollTop = document.documentElement.scrollHeight*%f" % j
#         #     driver.execute_script(js)
#         #     # 每次滚动等待0.5s
#         time.sleep(5)
#
#         # 获取下一页按钮的标签
#         # next_btn = driver.find_element_by_xpath('//span[contains(text(),"下一页")]')
#         # # 睡眠0.5秒
#         # time.sleep(0.5)
#         # # 对下一页标签进行鼠标右键触发事件
#         # ActionChains(driver).context_click(next_btn).click().perform()
#         # # driver.save_screenshot('截图.png')
#         # # 把驱动对象获得的源码赋值给新变量
#         page_source = dr.page_source
#         # 退出
#         dr.quit()
#
#         # 根据网页源代码,创建Htmlresponse对象
#         response = HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
#         # 因为返回的是文本消息,所以需要指定字符编码格式
#
#         return response

    # def process_response(self, request, response, spider):
    #     return response
    #
    # def process_exception(self, request, exception, spider):
    #     pass



























# from scrapy import signals
#
#
# class LalalaSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class LalalaDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # return None

    # def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # return response

    # def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        # pass

    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)
