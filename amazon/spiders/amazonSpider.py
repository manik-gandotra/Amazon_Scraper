import scrapy
import urllib
from amazon.items import AmazonItem
import os


class amazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    '''
    start_urls = ["http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=backpack",
                  "http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Abackpack&page=2&keywords=backpack&ie=UTF8&qid=1442907452&spIA=B00YCRMZXW,B010HWLMMA"
                  ]
    '''
    def start_requests(self):
        yield scrapy.Request("http://www.amazon.com/s/ref=sr_ex_n_3?rh=n%3A7141123011%2Cn%3A10445813011%2Cn%3A9479199011%2Cn%3A360832011&bbn=10445813011&ie=UTF8&qid=1442910853&ajr=0",self.parse)
        
        for i in range(2,3):
            yield scrapy.Request("http://www.amazon.com/s/ref=lp_360832011_pg_2?rh=n%3A7141123011%2Cn%3A10445813011%2Cn%3A9479199011%2Cn%3A360832011&page="+str(i)+"&bbn=10445813011&ie=UTF8&qid=1442910987",self.parse)
        
    
    
    def parse(self,response):
        namelist = response.xpath('//a[@class="a-link-normal s-access-detail-page s-overflow-ellipsis a-text-normal"]/@title').extract()
        #pricelist=response.xpath('//div[@class="a-row a-spacing-none"]').extract()
        listlength = len(namelist)
        for i in range(0,listlength):
            item = AmazonItem()
            item['Name'] = namelist[i]
            #item['Price']=pricelist[i]
            yield item
