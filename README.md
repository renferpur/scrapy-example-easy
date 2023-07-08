# scrapy-example-easy
Scrapy is a great tool to scrap web pages. It is a highly popular, fast, efficient, and easy-to-use framework. The official documentation is here.

    Speed: Scrapy is designed to be fast and efficient, so it can handle large amounts of data without slowing down.
    Extensibility: It is highly extensible, so you can customize it to fit your specific needs. You can write your own middleware, pipelines, and extensions to modify the behavior of Scrapy.
    Ease: It is easy to use, even for those who are new to web scraping. Its simple API and clear documentation make it easy to get started, and you can use it to build complex data pipelines with just a few lines of code.
    Robustness: It is built to handle a wide range of web scraping tasks, and it’s able to handle errors and exceptions gracefully. This makes it a reliable choice for scraping websites that may be prone to errors or changes.
    Community: Scrapy has an active community of users and developers, so you can find help and support if you run into any issues. There are also a large number of Scrapy extensions and integrations available, so you can easily expand the capabilities of your web scraper.

In this blog post, We will try to scrape http://books.toscrape.com/ URL. This is a fictional web page prepared for scrapping exercises.

You can find the project code here.
Installation

pip install Scrapy

After installing the library, we need to start a new project. I have created a root folder for my project named example. Inside this folder, I opened my terminal and created a virtual environment. I typed the below command in the terminal:

scrapy startproject example (example is my project name). It will create a project structure such below.
Project Structure. Image by the author.

Let’s go through these files one by one.
Spiders

They are classes that define how a website should be scraped. They are the core of the Scrapy system and are responsible for following links and extracting data from websites.

#book_spider.py

import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):
        title = response.css('title').extract()
        price = response.xpath("//p[@class='price_color']/text()").extract()

        yield {
            'title': title,
            'price': price,
        }

We create our own Spider classes by inheriting the Spider class from the library. We define selectors by overriding the parse method and returning data with the yield keyword.

The parse method takes a response object (<200 http://books.toscrape.com>)and breaks it down to gather the necessary information.

Type scrapy crawl books on the command line to run scraping. scrapy crawl command starts the engine and then we put the name of the spider. After you run the engine, you will see logs like below.
Terminal logs. Image by the author.
Yield

yield keyword yields a value and suspends the function’s execution, allowing it to be resumed later on, it is like return but with a different purpose. Whenreturn is used inside a function, it returns a value and terminates the function’s execution.

def foo(n):
    i = 0
    while i < n:
        yield i
        i += 1

f = foo(3)
print(type(f)) #<class 'generator'>

print(next(f)) #0
print(next(f)) #1
print(next(f)) #2

for i in foo(5):
    print(i)

"""
0
1
2
3
4
"""

Selectors

In Scrapy we can collect information from the page with two types of selectors: CSS selectors and XPath.

CSS

#CSS Selectors

#by TAG
title = response.css('title').extract()
#['<title>\n    All products | Books to Scrape - Sandbox\n</title>']
title = response.css('title')[0].extract()
#OR
title = response.css('title').extract_first()
#<title>
#    All products | Books to Scrape - Sandbox
#</title>

#get text, use :: to get att
title = response.css('title::text').extract()
#['\n    All products | Books to Scrape - Sandbox\n']

# tag + class + text
price = response.css('p.price_color::text').extract()
#['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']

#get elements that have a specific class
price = response.css('.price_color::text')[0].extract()
#£51.77

#nested elements (p tags inside a div)
price = response.css("div p.price_color").extract()
#['<p class="price_color">£51.77</p>', '<p class="price_color">£53.74</p>', '<p class="price_color">£50.10</p>', '<p class="price_color">£47.82</p>', '<p class="price_color">£54.23</p>', '<p class="price_color">£22.65</p>', '<p class="price_color">£33.34</p>', '<p class="price_color">£17.93</p>', '<p class="price_color">£22.60</p>', '<p class="price_color">£52.15</p>', '<p class="price_color">£13.99</p>', '<p class="price_color">£20.66</p>', '<p class="price_color">£17.46</p>', '<p class="price_color">£52.29</p>', '<p class="price_color">£35.02</p>', '<p class="price_color">£57.25</p>', '<p class="price_color">£23.88</p>', '<p class="price_color">£37.59</p>', '<p class="price_color">£51.33</p>', '<p class="price_color">£45.17</p>']

Xpath

#XPATH selectors

title = response.xpath("//title/text()").extract()
#['\n    All products | Books to Scrape - Sandbox\n']

price = response.xpath("//p[@class='price_color']").extract()
#{'price': ['<p class="price_color">£51.77</p>', '<p class="price_color">£53.74</p>', '<p class="price_color">£50.10</p>', '<p class="price_color">£47.82</p>', '<p class="price_color">£54.23</p>', '<p class="price_color">£22.65</p>', '<p class="price_color">£33.34</p>', '<p class="price_color">£17.93</p>', '<p class="price_color">£22.60</p>', '<p class="price_color">£52.15</p>', '<p class="price_color">£13.99</p>', '<p class="price_color">£20.66</p>', '<p class="price_color">£17.46</p>', '<p class="price_color">£52.29</p>', '<p class="price_color">£35.02</p>', '<p class="price_color">£57.25</p>', '<p class="price_color">£23.88</p>', '<p class="price_color">£37.59</p>', '<p class="price_color">£51.33</p>', '<p class="price_color">£45.17</p>']}

price = response.xpath("//p[@class='price_color']/text()").extract()
#['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']

#XPATH AND CSS TOGETHER
links = response.css("a").xpath("@href").extract()
#['\n    All products | Books to Scrape - Sandbox\n']

So, for our project, let’s scrape the title and the price of each book.

#book_spider.py

import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):
        products = response.css("li.col-xs-6")
        title = products.css("article h3 a::text").extract()
        price = products.css("p.price_color::text").extract()
        
        yield {
            'title': title,
            'price': price
        }

 #AND THE OUTPUT:
"""
{'title': ['A Light in the ...', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History ...', 'The Requiem Red', 'The Dirty Little Secrets ...', 'The Coming Woman: A ...', 'The Boys in the ...', 'The Black Maria', 'Starving Hearts (Triangular Trade ...', "Shakespeare's Sonnets", 'Set Me Free', "Scott Pilgrim's Precious Little ...", 'Rip it Up and ...', 'Our Band Could Be ...', 'Olio', 'Mesaerion: The Best Science ...', 'Libertarianism for Beginners', "It's Only the Himalayas"], 'price': ['£51.77', '£53.74', '£50.10', '£47.82', '£54.23', '£22.65', '£33.34', '£17.93', '£22.60', '£52.15', '£13.99', '£20.66', '£17.46', '£52.29', '£35.02', '£57.25', '£23.88', '£37.59', '£51.33', '£45.17']}
"""

Items

We use the Item class to store data. You can think of them as models in Django if you know what I mean. We move the scrapped data into a temporary container.

#items.py

import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()

We created two fields in the Item class.

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

After obtaining the products in the spider, we parse the information for each product with a for-loop. Rather than yielding this data in a dictionary, we pass them to an item object and yield it.
Export

We can export items in various formats.

Type scrapy crawl books -o items.json in the terminal and you get:


[
{"title": ["A Light in the ..."], "price": ["\u00a351.77"]},
{"title": ["Tipping the Velvet"], "price": ["\u00a353.74"]},
{"title": ["Soumission"], "price": ["\u00a350.10"]},
{"title": ["Sharp Objects"], "price": ["\u00a347.82"]},
{"title": ["Sapiens: A Brief History ..."], "price": ["\u00a354.23"]},
{"title": ["The Requiem Red"], "price": ["\u00a322.65"]},
{"title": ["The Dirty Little Secrets ..."], "price": ["\u00a333.34"]},
{"title": ["The Coming Woman: A ..."], "price": ["\u00a317.93"]},
{"title": ["The Boys in the ..."], "price": ["\u00a322.60"]},
{"title": ["The Black Maria"], "price": ["\u00a352.15"]},
{"title": ["Starving Hearts (Triangular Trade ..."], "price": ["\u00a313.99"]},
{"title": ["Shakespeare's Sonnets"], "price": ["\u00a320.66"]},
{"title": ["Set Me Free"], "price": ["\u00a317.46"]},
{"title": ["Scott Pilgrim's Precious Little ..."], "price": ["\u00a352.29"]},
{"title": ["Rip it Up and ..."], "price": ["\u00a335.02"]},
{"title": ["Our Band Could Be ..."], "price": ["\u00a357.25"]},
{"title": ["Olio"], "price": ["\u00a323.88"]},
{"title": ["Mesaerion: The Best Science ..."], "price": ["\u00a337.59"]},
{"title": ["Libertarianism for Beginners"], "price": ["\u00a351.33"]},
{"title": ["It's Only the Himalayas"], "price": ["\u00a345.17"]}
]

scrapy books -o items.xml

<?xml version="1.0" encoding="utf-8"?>
<items>
<item><title><value>A Light in the ...</value></title><price><value>£51.77</value></price></item>
<item><title><value>Tipping the Velvet</value></title><price><value>£53.74</value></price></item>
<item><title><value>Soumission</value></title><price><value>£50.10</value></price></item>
<item><title><value>Sharp Objects</value></title><price><value>£47.82</value></price></item>
<item><title><value>Sapiens: A Brief History ...</value></title><price><value>£54.23</value></price></item>
<item><title><value>The Requiem Red</value></title><price><value>£22.65</value></price></item>
<item><title><value>The Dirty Little Secrets ...</value></title><price><value>£33.34</value></price></item>
<item><title><value>The Coming Woman: A ...</value></title><price><value>£17.93</value></price></item>
<item><title><value>The Boys in the ...</value></title><price><value>£22.60</value></price></item>
<item><title><value>The Black Maria</value></title><price><value>£52.15</value></price></item>
<item><title><value>Starving Hearts (Triangular Trade ...</value></title><price><value>£13.99</value></price></item>
<item><title><value>Shakespeare's Sonnets</value></title><price><value>£20.66</value></price></item>
<item><title><value>Set Me Free</value></title><price><value>£17.46</value></price></item>
<item><title><value>Scott Pilgrim's Precious Little ...</value></title><price><value>£52.29</value></price></item>
<item><title><value>Rip it Up and ...</value></title><price><value>£35.02</value></price></item>
<item><title><value>Our Band Could Be ...</value></title><price><value>£57.25</value></price></item>
<item><title><value>Olio</value></title><price><value>£23.88</value></price></item>
<item><title><value>Mesaerion: The Best Science ...</value></title><price><value>£37.59</value></price></item>
<item><title><value>Libertarianism for Beginners</value></title><price><value>£51.33</value></price></item>
<item><title><value>It's Only the Himalayas</value></title><price><value>£45.17</value></price></item>
</items>

scrapy books -o items.csv

price,title
£51.77,A Light in the ...
£53.74,Tipping the Velvet
£50.10,Soumission
£47.82,Sharp Objects
£54.23,Sapiens: A Brief History ...
£22.65,The Requiem Red
£33.34,The Dirty Little Secrets ...
£17.93,The Coming Woman: A ...
£22.60,The Boys in the ...
£52.15,The Black Maria
£13.99,Starving Hearts (Triangular Trade ...
£20.66,Shakespeare's Sonnets
£17.46,Set Me Free
£52.29,Scott Pilgrim's Precious Little ...
£35.02,Rip it Up and ...
£57.25,Our Band Could Be ...
£23.88,Olio
£37.59,Mesaerion: The Best Science ...
£51.33,Libertarianism for Beginners
£45.17,It's Only the Himalayas

Middleware

Middleware is a layer between the Scrapy engine and your spiders that allows you to perform custom processing on requests and responses as they are passed between the engine and the spiders. For example, if you will add proxies to requests, you will do it through middleware.
Pipeline

Pipeline classes are responsible for processing the items scraped by your spiders.

Procedurally, we first scrapped the data in spiders, then stored them in items. The next step is the pipeline. We decide how we will store the data we collect.

#settings.py

#active pipeline by adding this (or uncomment)
ITEM_PIPELINES = {
   'example.pipelines.ExamplePipeline': 300,
}

#300 is the priority index, lower is more prioritized.

import sqlite3

class ExamplePipeline:

    def __init__(self):
        self._initialize_connection()

    def _initialize_connection(self):
        """database work"""
        self.__connect()
        self.__create_db_table()

    def __connect(self):
        """connect (or create) sqlite db"""
        self.con = sqlite3.connect("books.db")
        self.cur = self.con.cursor()
        return

    def __create_db_table(self):
        """create table"""
        self.cur.execute("DROP TABLE IF EXISTS booktable")
        self.cur.execute("create table booktable (title text, price tag)")
        return
    
    def __insert(self, item):
        """insert new records"""
        self.cur.execute("insert into booktable values (?,?)", (item["title"][0], item["price"][0]))
        self.con.commit()
        return

    def process_item(self, item, spider):
        self.__insert(item)
        return item

In the process_item method, we define what to do with the scrapped data. In the above example, we insert them into an SQLite database.
SQLite database. Image by the author.
Settings

It contains the settings that are used by the framework when running the project. The settings can be used to customize the behavior, such as how the spider should crawl the web, how it should handle requests and responses, and what pipelines should be used to process the data that is scraped.

#settings.py

# Scrapy settings for example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'example (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'example.middlewares.ExampleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'example.middlewares.ExampleDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'example.pipelines.ExamplePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

BOT_NAME = 'example'. Automating an action that works on the web is called a bot. So, we declare the name of our bot. This is used to identify the bot when making requests to web servers.

#A list of module names that contain the spider classes.
SPIDER_MODULES = ['example.spiders']

#The module name where Scrapy should look for new spiders.
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT is sent as part of an HTTP request header, which identifies the client that is making the request. This can be used by the server to customize the response based on the type of client that is making the request. Whenever you visit a web page, you need to identify yourself.

You can ask “what is my user agent” to Google?
What is my user agent? Image by the author.

#settings.py
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html'

We can use different user agents. We will use the scrapy-user-agents library.

pip install scrapy-user-agents

#settings.py

#ADD
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = True statement determines whether to obey the robots.txt file on the target website. The robots.txt file is a text file that web servers use to communicate with web robots (also known as "bots" or "spiders") about which pages or files the robot is allowed to access. For example, in the URL: https://www.facebook.com/robots.txt you can find the robots that are disallowed by Facebook.
Robots.txt. Source

CONCURRENT_REQUESTS=32. Scrapy can work concurrently. We can specify the concurrent request amount. Drive responsibly.

COOKIES_ENABLED determines whether to send cookies with requests.

DEFAULT_REQUEST_HEADERS is a dictionary that contains the header information of every request.

AUTOTHROTTLE feature is a built-in mechanism that helps to regulate the speed at which a Scrapy spider crawls a website.

#settings.py

#whether the autothrottle feature should be enabled
AUTOTHROTTLE_ENABLED = True

#the initial delay (in seconds) that should be used before the first request is made.
AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

Shell

You can run your commands in Scrapy Shell. It can be very useful to be able to test the elements on a page and how we can get them, and to find our way around.

Type scrapy shell "http://books.toscrape.com" and press enter. It will open up the shell. You can run your commands in this shell.
Scrapy Shell. Image by the author.
Following a Link

#book_spider.py

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

We parse the href attribute from the next button. The follow method helps us to navigate into another URL. We also set a callback function, in our case, we want it to parse the same info for each following page.
Proxy

A proxy routes your request to a website through its own IP address, which makes it look like the request is coming from the proxy instead of your computer.

We can use proxies in a Scrapy project via the scrapy-proxy-pool library.

pip install scrapy_proxy_pool

#settings.py
PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES= {
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
}

Conclusion

In conclusion, Scrapy is a powerful and useful Python library for web scraping. It allows you to easily extract data from websites and process it in a convenient format. With its efficient and fast web crawling capabilities, Scrapy is an essential tool for data scientists, researchers, and anyone looking to gather and analyze large amounts of data from the web. Whether you’re a beginner or an experienced programmer, Scrapy is a valuable addition to your toolkit.
