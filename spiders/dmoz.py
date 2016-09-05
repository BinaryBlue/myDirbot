from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.w3newspapers.com/bangladesh/",
        "http://www.allbanglanewspaperlist24.com/",
        "http://allbanglanewspapers.com/",
        "http://onlinebanglanewspaperlist.com/",
        "http://news.creative.com.bd/",
        "http://banglaonlinenews.com/",
        "http://www.banglanewslive.com/",
        "https://en.wikipedia.org/wiki/List_of_newspapers_in_Bangladesh",
        "http://bdwebguide.com/",
        "http://www.allnewspaperlist.com/bangla-newspaper.html",

    ]

    def parse(self, response):
        sel = Selector(response)
        #sites = sel.xpath('//ul/li')
        sites = response.css('a')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('@title').extract()
            item['url'] = site.xpath('@href').extract()
            items.append(item)

        return items
