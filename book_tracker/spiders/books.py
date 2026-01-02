import scrapy
from book_tracker.items import BookTrackerItem


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        self.logger.info("Spider is running at URL=%s", response.url)
        item = BookTrackerItem()
        # .get() is safe. will return None if nothing is found. Cool
        item["url"] = response.url
        item["title"] = response.css("title::text").get()

        yield item
