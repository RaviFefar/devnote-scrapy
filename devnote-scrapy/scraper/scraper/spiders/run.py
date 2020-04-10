import scrapy

from student.models import BlogPost
from scraper.items import BlogPostItem
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule

class DevnoteSpider(scrapy.Spider):
    name = 'devnote'
    allowed_domains = ["devnote.in"]
    start_urls = ('https://devnote.in/',)

    """Rules = (
        Rule(
            LinkExtractor(
            allow=(),
            restrict_xpaths=('//a[@class="next page-numbers"]',)
            ),
        callback="parse",
        follow= True
        ),
    )"""

    def parse(self, response):
        for idx, values in enumerate(response.css("#main_post_display .home-page-column")):
            post = BlogPostItem()

            title = values.css("h4 a::text").extract_first()
            image = values.css(".featured-image img, .language-image-home img").xpath("@src").extract_first()
            count_p_a = len(values.css(".entry-categories p a::text"))
            category_p_a = values.css(".entry-categories p a::text").extract()

            categories_join = ""
            for i, data_p in enumerate(category_p_a):
                categories_join += data_p.join(" ,")

            categories = categories_join.rstrip(" ,")

            #Database save
            post['name'] = title
            post['image'] = image
            post['category'] = categories

            yield post

        # Verify if contains more pages
        """next_page = response.xpath('//a[@class="page-numbers"]/@href').extract_first()
        if next_page:
            request = scrapy.Request(url=next_page)
            yield request"""

