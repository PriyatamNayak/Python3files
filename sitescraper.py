import scrapy

class SiteScraper(scrapy.Spider):
	name = "sitescraper"
	def start_requests(self):
		urls = ["http://www.bogotobogo.com/python/scikit-learn/scikit_machine_learning_Data_Preprocessing-Missing-Data-Categorical-Data.php",
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = '%s.html' % page
		with open (filename,"wb") as f:
			f.write(response.body)
		self.log("Saved File %s" %filename)