import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        quote = self.extract_quote(response)
        yield quote

    def extract_quote(self, response):
        return {
            'text': self.extract_with_css(response, 'span.text::text'),
            'author': self.extract_with_css(response, 'small.author::text'),
            'tags': self.extract_tags(response),
        }

    def extract_with_css(self, response, query):
        return response.css(query).get(default='').strip()

    def extract_tags(self, response):
        return response.css('div.tags a.tag::text').getall()
