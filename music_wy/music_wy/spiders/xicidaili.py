import time
import scrapy
import sys
import datetime

sys.path.append('C:\\Users\\wang\\Desktop\\haveafun\\fortb\\music_wy\\music_wy')

from fortb.music_wy.music_wy import ipproxy


class xicidaili(scrapy.Spider):
    name = 'xicidaili'
    base_url = "http://www.xicidaili.com/nn/"
    allowed_domains = ["www.xicidaili.com"]

    start_page = 51
    max_page = 500
    start_urls = ["http://www.xicidaili.com/nn/%s" % start_page]

    def parse(self, response):
        tr_list = response.css('table#ip_list tr:nth-of-type(n+2)')
        obj_ipproxy = ipproxy.ipproxy()
        for tr in tr_list:
            item = {
                'ip': tr.css('td:nth-of-type(2)::text').extract_first(default=0),
                'port': tr.css('td:nth-of-type(3)::text').extract_first(default=0),
            }
            alive = tr.css('td:nth-of-type(9)::text').extract_first(default=0)
            update_time = tr.css('td:nth-of-type(10)::text').extract_first(default=0)

            item['deadline'] = self.get_deadline(alive, update_time)
            start = time.time()
            if datetime.datetime.now() > item['deadline']:
                print('deadline %s' % item['ip'])
                continue
            if item['ip'] != 0 and obj_ipproxy.check_ip(item):
                item['delay'] = time.time() - start
                yield item
        count = response.meta.get('count', self.start_page + 1)
        print('current page: %s' % count)
        if count <= self.max_page:
            next_url = self.base_url + str(count)
            yield scrapy.Request(next_url,  # 请求的url
                                 callback=self.parse,  # 回调函数
                                 meta={'count': count + 1}  # 传 递参数
                                 )

    def check_lest_time(self):
        pass

    @staticmethod
    def get_deadline(alive, update_time):
        dic = {
            "天": "days",
            "小时": "hours",
            "分钟": "minutes"
        }
        format_time = datetime.datetime.strptime('20' + str(update_time), '%Y-%m-%d %H:%M')
        for key, item in dic.items():
            if key in alive:
                stamp = int(alive[:-(len(key))])
                if item == 'days':
                    format_time += datetime.timedelta(days=+stamp)
                elif item == 'hours':
                    format_time += datetime.timedelta(hours=+stamp)
                elif item == 'minutes':
                    format_time += datetime.timedelta(minutes=+stamp)
                else:
                    format_time = 0
        return format_time
