# to save cvs format run file  as scrapy crawl spider_name -o filename.csv    or -o filename.json
import scrapy

class Nse(scrapy.Spider):
	name = "nse"
	def start_requests(self):
		urls = ["https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm?cat=N",
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self,response):
		for data in response.css("div.allWatches"):
			yield {
				"info": data.css("ul.links::text").extract_first(),
				
			}
		next1 = response.css('li.Download in CSV a::attr(href)').extract_first()
		if next1 is not None:
			next1 = response.urljoin(next1)
			yield scrapy.Request(next1, callback = self.parse)

	



	#def parse(self, response):
	#	page = response.url.split("/")[-2]
	#	filename = '%s.html' % page
	#	with open (filename,"wb") as f:
	#		f.write(response.body)
	#	self.log("Saved File %s" %filename)