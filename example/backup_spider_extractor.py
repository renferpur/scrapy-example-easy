import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):
        #print("Response: ",response) #Response:  <200 http://books.toscrape.com>

        #CSS Selector
        #by tag
        #title = response.css('title')[0].extract()
        #{'title': ['<title>\n    All products | Books to Scrape - Sandbox\n</title>']}

        #by tag get text
        #title = response.css('title::text').extract()
        #{'title': ['\n    All products | Books to Scrape - Sandbox\n']}

        #get first element in the list
        #title = response.css('title::text')[0].extract()
        #title = response.css('title::text').extract_first()
        #'\n    All products | Books to Scrape - Sandbox\n'
        
        #css + tag + class
        #price = response.css('p.price_color::text').extract()
        #['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']
        
        #css + only class
        #price = response.css('.price_color::text')[0].extract()
        #£51.77

        #css nested elements
        #price = response.css("div p.price_color").extract()

        #XPATH SELECTOR

        #title = response.xpath("//title/text()").extract()

        #links = response.css("a").xpath("@href").extract()
        #['\n    All products | Books to Scrape - Sandbox\n']
        
        price = response.xpath("//p[@class='price_color']/text()").extract()
        #['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']
        print("****")
        print(price)
        print("*****")
        yield { 
            'price': price,
        }

