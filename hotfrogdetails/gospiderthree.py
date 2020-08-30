from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hotfrogdetails.spiders.hotfrogthree import HotfrogthreeSpider


process = CrawlerProcess(get_project_settings())
process.crawl(HotfrogthreeSpider)
process.start()
