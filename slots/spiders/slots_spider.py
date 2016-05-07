import scrapy

from slots.items import SlotsItem

class SlotsSpider(scrapy.Spider):
    name = "slots"
    allowed_domains = ["luckymobileslots.com"]
    start_urls = [
        "http://www.luckymobileslots.com/?s=",
    ]
         
    def parse(self, response):
        # Identifies all links in the search-list class while excluding the adverts.
        for href in response.xpath('//body/div/div/div/ul/li/a/@href'):
            url = response.urljoin(href.extract())
            substring = "game-reviews"
            if substring in url:
                yield scrapy.Request(url, callback=self.parse_page_contents)

        # Adds Requests for all pages in the pagination.
        next_page = response.xpath('//div[@class="pagination"]/a[@class="next"]/@href').extract()[0]
        if next_page:
            next_page_url = response.urljoin(next_page)
            print next_page_url
            yield scrapy.Request(next_page_url, callback=self.parse)

    # Parses the required information from every subpage.
    def parse_page_contents(self, response):
        sel = response.xpath('//div[@class="overview"]/table/tbody/tr/td[@class="value"]/text()').extract()
        sel1 = response.xpath('//*[@id="jumbo-internal"]/div/div[2]/span/text()').extract()
        sel2 = response.xpath('//*[@id="jumbo-internal"]/div/div[2]/h1/text()').extract()
        item = SlotsItem()
        item['title'] = sel2[0]
        item['software'] = sel1[0]
        item['slot_reels'] = sel[2]
        item['volatility'] = sel[4]
        item['coins_range'] = sel[5]

        sel3 = response.xpath('//*[@id="review-wrapper"]/div[2]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()

        item['jackpot'] = sel3[0]

        sel4 = response.xpath('//*[@id="review-wrapper"]/div[2]/div/div/div[1]/div[2]/table/tbody/tr[9]/td[2]/text()').extract()

        for element in sel4:
            item['bonus'] = element

        yield item
