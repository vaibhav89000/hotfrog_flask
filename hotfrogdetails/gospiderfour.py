from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hotfrogdetails.spiders.hotfrogfour import HotfrogfourSpider


process = CrawlerProcess(get_project_settings())
process.crawl(HotfrogfourSpider)
process.start()
