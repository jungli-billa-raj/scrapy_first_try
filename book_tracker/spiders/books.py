import scrapy
# from book_tracker.items import BookTrackerItem


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # follow product links
        for href in response.css("article.product_pod h3 a::attr(href)").getall():
            yield response.follow(href, callback=self.parse_book)

        # follow pagination
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        self.logger.info("Visited site: %s", response.url)

        book_description = response.css("article.product_page > p::text").get()
        book_title = response.css("article.product_page h1::text").get()

        if book_description and book_title:
            self.logger.info("Book Title: %s", book_title)
            self.logger.info("Book Description: %s", book_description)
