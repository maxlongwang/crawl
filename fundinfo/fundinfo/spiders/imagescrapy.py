import scrapy
import scrapy.spiderloader
from fundinfo.items import ImageChinazItem
import re
# 使用

class ImageSpider(scrapy.Spider):
    name = 'imagespider'
    start_urls = ["https://sc.chinaz.com/"]

    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 300},
                       # 图片过滤器，最小高度和宽度，低于此尺寸不下载
                    #    'IMAGES_MIN_HEIGHT': 110,
                    #    'IMAGES_MIN_WIDTH': 110,
                       # 图片过滤器，最小高度和宽度，低于此尺寸不下载
                    #    'IMAGES_THUMBS': {'small': (50, 50),
                    #                      'big': (250, 250), }

                       }

    def parse(self, response):
        # sel=scrapy.Selector(response)
        url_list = []
        item = ImageChinazItem()
        # image_urls = response.xpath('//div//a[@href]/img/@src').extract()
        # for url in image_urls:
        #     url_full=response.urljoin(url)
        #     url_list.append(url_full)

        text = response.body.decode('utf-8')
        pattern = re.compile(r'src="(.*\.(jpg|jpeg|png|gif|bmp))"')
        urls = re.findall(pattern, text)
        for url, _ in urls:
            url = response.urljoin(url)
            url_list.append(url)

        item['image_urls'] = url_list
        yield item
