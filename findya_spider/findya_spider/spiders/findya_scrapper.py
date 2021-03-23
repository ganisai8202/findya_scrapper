import scrapy


class FindyaScrapperSpider(scrapy.Spider):
    name = 'findya_scrapper'

    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']


    def parse(self,response):
        item_urls=response.css('li::attr(data-url)').extract()

        for url in item_urls:
            yield scrapy.Request(url, callback = self.parse2)



    def parse2(self, response):

        description=response.xpath('//*[@id="tab-1"]/p/text()').get()
        price=response.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div[2]/h4//text()').extract()[3].strip()
        name=response.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div[2]/h1/text()').get()
        image_url=response.xpath('//*[@id="productsections"]/ul/li[1]/a/@data-image').get()

        scraped_info={
                'title':name,
                'price':price,
                'description':description,
                'image_url':image_url
                }

        yield scraped_info
