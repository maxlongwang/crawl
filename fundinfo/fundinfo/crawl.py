
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

print(get_project_settings())

# process.crawl('fundprod')
# process.crawl('fundmanager')
# process.crawl('futuresprod')
# process.crawl('futuresmanager')
# process.crawl('collectasset')
# process.crawl('secucollectasset')
# process.crawl('pdftest1')
# process.crawl('pandamusic')
# process.crawl('pandamusicdy')
process.crawl('pandamusicrd2')


process.start()

