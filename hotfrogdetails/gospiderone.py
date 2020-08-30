from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hotfrogdetails.spiders.hotfrog import HotfrogSpider


process = CrawlerProcess(get_project_settings())
process.crawl(HotfrogSpider)
process.start()
