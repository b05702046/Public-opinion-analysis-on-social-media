import scrapy
import html2text
import logging
import re


from datetime import datetime
from scrapy.http import FormRequest
from ptt.items import PostItem


class PTTSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.cc']
    start_urls = ('https://www.ptt.cc/bbs/Gossiping/index2800.html', )

    _retries = 0
    MAX_RETRY = 1

    _pages = 0
    MAX_PAGES = 3000

    def parse(self, response):
        if len(response.xpath('//div[@class="over18-notice"]')) > 0:
            if self._retries < PTTSpider.MAX_RETRY:
                self._retries += 1
                logging.warning('retry {} times...'.format(self._retries))
                yield FormRequest.from_response(response,
                                                formdata={'yes': 'yes'},
                                                callback=self.parse)
            else:
                logging.warning('you cannot pass')

        else:
            self._pages += 1
            for href in response.css('.r-ent > div.title > a::attr(href)'):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_post)

            if self._pages < PTTSpider.MAX_PAGES:
                next_page = response.xpath(
                    '//div[@id="action-bar-container"]//a[contains(text(), "上頁")]/@href')
                if next_page:
                    url = response.urljoin(next_page[0].extract())
                    logging.warning('follow {}'.format(url))
                    yield scrapy.Request(url, self.parse)
                else:
                    logging.warning('no next page')
            else:
                logging.warning('max pages reached')

    def parse_post(self, response):
        item = PostItem()
        item['ID'] = re.findall(r'https://www.ptt.cc/bbs/Gossiping/(\w.\d+.\w.\S+).html', response.url)[0]
        item['title'] = response.xpath('//meta[@property="og:title"]/@content')[0].extract()
        item['kanban'] = response.xpath('//div[@class="article-metaline-right"]/span[text()="看板"]/following-sibling::span[1]/text()')[0].extract()
        item['author'] = response.xpath('//div[@class="article-metaline"]/span[text()="作者"]/following-sibling::span[1]/text()')[0].extract().split(' ')[0]
        item['date'] = response.xpath('//div[@class="article-metaline"]/span[text()="時間"]/following-sibling::span[1]/text()')[0].extract()

        # 處理內文
        regex_content = r'<span class="article-meta-tag">時間<\/span><span class="article-meta-value">.*<\/span><\/div>([\s\S]+)--'
        content = response.xpath('//div[@id="main-content"]')[0].extract()
        content = re.findall(regex_content, content)[0]

        converter = html2text.HTML2Text()
        converter.ignore_links = True
        item['content'] = converter.handle(content)

        # 處理回文
        push = []
        shush = []
        reply = []
        for comment in response.xpath('//div[@class="push"]'):
            push_tag = comment.css('span.push-tag::text')[0].extract()
            push_content = comment.css('span.push-content::text')[0].extract()

            if '推' in push_tag:
                push.append(push_content.replace(': ', ''))
            elif '噓' in push_tag:
                shush.append(push_content.replace(': ', ''))
            else:
                reply.append(push_content.replace(': ', ''))

        item['push'] = str(push)
        item['shush'] = str(shush)
        item['reply'] = str(reply)

        yield item
