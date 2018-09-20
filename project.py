# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import MusicItem

class ProjectSpider(scrapy.Spider):
    name = 'project'
    allowed_domains = ['music.163.com']

    start_urls = ['https://music.163.com/discover/playlist']

    def parse(self, response):
    	#找到所有歌单分类的链接
    	links = response.xpath('//*[@id="cateListBox"]/div[2]/dl')
    	for link in links:
    		#所有的一级分类
    		one_class = link.xpath('dt/text()').extract()
    		#所有的二级分类
    		two_class = link.xpath('dd/a/text()').extract()
    		#所有二级分类下的歌单风格链接
    		link = link.xpath('dd/a/@href').extract()
    		for url,two in zip(link,two_class):
    			url = "https://music.163.com"+url
    			#将一级分类中的二级分类界面URL传递下去
    			yield scrapy.Request(url,callback=self.music,meta={'one_class':one_class,'two_class':two})
    def music(self,response):
    	#找到二级分类下的歌单列表URL传递下去
    	links = response.xpath('//*[@id="m-pl-container"]/li/p[1]/a/@href').extract()
    	for link in links:
    		url="https://music.163.com"+link
    		yield scrapy.Request (url,callback=self.detail,meta=response.meta)
    	next_url=response.xpath('//a[text()="下一页"]/@href').extract_first()
    	if next_url:
    		next_url="https://music.163.com"+next_url
    		yield scrapy.Request(next_url,callback=self.music,meta=response.meta)
    def detail(self,response):
    	item = MusicItem()
    	item['one_class'] = response.meta['one_class']
    	item['two_class'] = response.meta['two_class']
    	item['music_img'] = response.xpath('//*[@class="m-info f-cb"]/div[1]/img/@src').extract_first()
    	item['play_number'] = response.xpath('//*[@class="more s-fc3"]/strong/text()').extract_first()
    	item['music_author'] = response.xpath('//*[@class="cntc"]/div[2]/span[1]/a/text()').extract_first()
    	item['music_list_introduce'] = response.xpath('//*[@class="cntc"]/p/text()').extract_first()
    	item['music_author_id'] = response.xpath('//*[@class="cntc"]/div[2]/span[1]/a/@href').extract_first()
    	item['music_list'] = response.xpath('//*[@class="tit"]/h2/text()').extract_first()
    	yield item
