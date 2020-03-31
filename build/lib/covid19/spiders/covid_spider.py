import scrapy
from ..items import covid19Item
from datetime import datetime


class QuoteSpider(scrapy.Spider):
    name = 'covid19'
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]

    # def parse(self, response):
    #     all_div_quotes = response.css('.quote')
    #
    #     for quotes in all_div_quotes:
    #         title = quotes.css('.text::text').extract()
    #         author = quotes.css('.author::text').extract()
    #         tags = quotes.css('.tag::text').extract()
    #         yield {
    #             'title': title,
    #             'author': author,
    #             'tags': tags
    #         }

    def parse(self, response):
        items = covid19Item()

        all_countries_stats = response.xpath('//*[@id="main_table_countries_today"]//tbody//tr')

        for row in all_countries_stats:
            country = row.xpath('td[1]//text()').extract_first().strip()
            total_cases = str(row.xpath('td[2]//text()').extract_first()).strip()
            new_cases = str(row.xpath('td[3]//text()').extract_first()).strip()
            total_deaths = str(row.xpath('td[4]//text()').extract_first()).strip()
            new_deaths = str(row.xpath('td[5]//text()').extract_first()).strip()
            total_recovered = str(row.xpath('td[6]//text()').extract_first()).strip()
            active_cases = str(row.xpath('td[7]//text()').extract_first()).strip()
            critical_cases = str(row.xpath('td[8]//text()').extract_first()).strip()
            last_updated = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

            items['country'] = country
            items['total_cases'] = total_cases
            items['new_cases'] = new_cases
            items['total_deaths'] = total_deaths
            items['new_deaths'] = new_deaths
            items['total_recovered'] = total_recovered
            items['active_cases'] = active_cases
            items['critical_cases'] = critical_cases
            items['last_updated'] = last_updated

            yield items
