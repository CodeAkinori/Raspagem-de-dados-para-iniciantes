import scrapy
import json

class InfiniteScrollSpider(scrapy.Spider):
    name = 'infinite_scroll'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data.get('quotes', []):
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags'],
            }

        if data.get('has_next'):
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
