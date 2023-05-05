import scrapy

class BooksBasicSpider(scrapy.Spider):
    name = "books_basic"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/business_35/index.html"]

    def parse(self, response):
        sel=scrapy.Selector(response)
        articles=sel.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article')
        for article in articles:
            title=article.xpath('//h3/a/@title').extract()
            price=article.xpath('//div[2]/p[1]/text()').extract()
            thumbnail=article.xpath('//div[1]/a/img/@src').extract()
        yield{
            'title':title,
            'price':price,
            'thumbnail':thumbnail,
        }
