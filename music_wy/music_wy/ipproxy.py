import json
from random import choice
import requests
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout


class ipproxy(object):
    proxy = []

    def __init__(self):
        with open('./tmp/ip.json', 'r') as f:
            self.proxy = json.load(f)

    def get_ip(self):
        return self.proxy

    def get_random_ip(self):
        return choice(self.proxy)

    def check_ip(self, ip_item):
        try:
            tmp = requests.get('http://www.baidu.com', proxies={'http': '%s:%s' % (ip_item['ip'], ip_item['port'])},
                               timeout=2)
            checked = True
        except(BaseException, ProxyError, ConnectTimeout, ReadTimeout):
            checked = False
        return checked


if __name__ == '__main__':
    proxy = ipproxy()
    count = 0
    for val in proxy.get_ip():
        if proxy.check_ip(val):
            print('success %s:%s' % (val['ip'], val['port']))
        else:
            count += 1
            print("error %s  %s:%s" % (count, val['ip'], val['port']))
