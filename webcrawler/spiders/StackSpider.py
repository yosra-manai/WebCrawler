from scrapy import Spider
from scrapy.selector import Selector
from webcrawler.items import WebcrawlerItem

class StackSpider(Spider):
	name = "stack"
	allowed_domains = ["placesonline.com"]
	start_urls = [
		"http://www.placesonline.com/africa/tunisia/places.asp",
	]
	
	def parse(self, response):
		places = Selector(response).xpath('//*[@id="content"]')
       
		for place in places:
			item = WebcrawlerItem()
			item['title'] = place.xpath(
				'div[22]/div[1]/a/text()').extract()[0]
			item['url'] = place.xpath(
				'div[22]/div[1]/a/@href').extract()[0]
			item['rate'] = place.xpath(
				'div[22]/div[2]/div[2]/span/text()').extract()[0]
			
			yield item
 
        