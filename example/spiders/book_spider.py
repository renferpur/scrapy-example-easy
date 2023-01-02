import scrapy
from ..items import BookItem


class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):

        items = BookItem()

        #scrap product elements
        products = response.css("li.col-xs-6")

        for book in products:
            title = book.css("article h3 a::text").extract()
            price = book.css("p.price_color::text").extract()
            items["title"] = title
            items["price"] = price

            yield items

        #get the url of the next page from the next button
        next_page_link = response.css("li.next a::attr(href)").get()
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)
        