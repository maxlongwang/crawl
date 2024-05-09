
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# process.crawl('fundprod')
# process.crawl('fundmanager')
# process.crawl('futuresprod')
# process.crawl('futuresmanager')
# process.crawl('collectasset')
process.crawl('secucollectasset')

process.start()
