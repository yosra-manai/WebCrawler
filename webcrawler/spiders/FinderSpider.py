from scrapy import Spider
from scrapy.selector import Selector
from webcrawler.items import WebcrawlerItem

class FinderSpider(Spider):
	name = "Finder"
	allowed_domains = ["tripadvisor.com"]
	start_urls = [
		"http://www.tripadvisor.com/Tourism-g293753-Tunisia-Vacations.html",
	]
	
	def parse(self, response):
		places = Selector(response).xpath('//*[@id="BODYCON"]/div[2]/div/div/div[2]')
       
		for place in places:
			item = WebcrawlerItem()
			item['title'] = place.xpath(
				'a[6]/div[2]/div/span[2]/text()').extract()[0]
			item['url'] = place.xpath(
				'a[6]/@href').extract()[0]
			item['rate'] = place.xpath(
				'a[6]/div[2]/div/span[1]/text()').extract()[0]
			
			yield item
 
        