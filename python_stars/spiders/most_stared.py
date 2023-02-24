import scrapy
import scraper_helper as sh

URL = 'https://github.com/search?l=&o=desc&q=python&s=stars&type=Repositories'

class MostStaredSpider(scrapy.Spider):
    name = 'most_stared'

    def start_requests(self):
        yield scrapy.Request(URL)

    def parse(self, response):
        item = {}
        for repo in response.css('.repo-list-item'):
            item['name'] = repo.css('.v-align-middle ::text').get()
            str_stars = repo.css('.mr-3 .Link--muted ::text').extract()
            str_stars = ''.join(str_stars)
            item['stars'] = sh.cleanup(str_stars)
            yield item

        next_page = response.xpath('//a[text()="Next"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
