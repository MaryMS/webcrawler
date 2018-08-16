from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from urls.items import UrlItem

class GetLinksSpider(CrawlSpider):
    
    #Crawl name
    name = 'getlink'
    
    #allowed_domains = ['g1.globo.com']
   
    #URL que inicia o crawling.
    start_urls = ['http://g1.globo.com/']
    
    #Regras de navegação entre os links
    rules = (
        Rule(LinkExtractor(), callback='parse_url', follow=True),
    )

    #Retorna a URL
    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url
    
        return item

        






   


