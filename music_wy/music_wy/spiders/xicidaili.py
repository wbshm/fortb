import time
import scrapy
import sys

sys.path.append('C:\\Users\\wang\\Desktop\\haveafun\\fortb\\music_wy\\music_wy')

from fortb.music_wy.music_wy import ipproxy


class xicidaili(scrapy.Spider):
    name = 'xicidaili'
    start_urls = ["http://www.xicidaili.com/nn/1"]
    base_url = "http://www.xicidaili.com/nn/"
    allowed_domains = ["www.xicidaili.com"]

    max_page = 100

    def parse(self, response):
        tr_list = response.css('#ip_list tr')
        obj_ipproxy = ipproxy.ipproxy()
        for tr in tr_list:
            item = {'ip': tr.css('td:nth-child(2)::text').extract_first(default=0),
                    'port': tr.css('td:nth-child(3)::text').extract_first(default=0)}
            start = time.time()
            if obj_ipproxy.check_ip(item) and item['ip'] != 0:
                item['delay'] = time.time() - start
                yield item
        count = response.meta.get('count', 2)
        if count <= self.max_page:
            next_url = self.base_url + str(count)
            yield scrapy.Request(next_url,  # 请求的url
                                 callback=self.parse,  # 回调函数
                                 meta={'count': count + 1}  # 传递参数
                                 )
