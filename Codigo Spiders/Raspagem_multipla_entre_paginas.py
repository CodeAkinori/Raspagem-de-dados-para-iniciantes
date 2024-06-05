import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):     
            caixa = {
                'autor': quote.css('small.author::text').extract_first(),
                'texto': quote.css('span.text::text').extract_first(),
                'categorias': quote.css('a.tag::text').extract(),
            }
            yield caixa

        proxima_pag = response.css('li.next > a::attr(href)').extract_first()
        if proxima_pag:
            proxima_pag = response.urljoin(proxima_pag)
            yield scrapy.Request(url=proxima_pag, callback=self.parse)
