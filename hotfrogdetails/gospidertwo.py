from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hotfrogdetails.spiders.hotfrogtwo import HotfrogtwoSpider


process = CrawlerProcess(get_project_settings())
process.crawl(HotfrogtwoSpider)
process.start()
