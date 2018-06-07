import scrapy

class FirstSpider(scrapy.Spider):
	name = "first"
	def start_requests(self):
		urls = ['http://quotes.toscrape.com/page/1/',
				
		]
		for url in urls:
			yield scrapy.Request(url =url, callback = self.parse)
			
	def parse(self,response):
		for quote in response.css('div.quote'):
			yield {
				'text': quote.css('span.text::text').extract_first(),
				'author': quote.css('small.author::text').extract_first(),
			}

		next1 = response.css('li.next a::attr(href)').extract_first()
		if next1 is not None:
			next1 = response.urljoin(next1)
			yield scrapy.Request(next1, callback = self.parse)
