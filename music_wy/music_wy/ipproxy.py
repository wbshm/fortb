import json
from random import choice
import requests
from requests.exceptions import ProxyError


class ipproxy:
    def get_ip(self):
        proxy = ""
        with open('./tmp/ip.json', 'r') as f:
            proxy = json.load(f)
        if proxy:
            return choice(proxy)

    def check_ip(self):
        ip_proxy = self.get_ip()
        print('%s:%s' % (ip_proxy['ip'], ip_proxy['port']))
        try:
            tmp = requests.get('http://localhost', proxies={'http': '%s:%s' % (ip_proxy['ip'], ip_proxy['port'])})
        except ProxyError:
            print('ProxyError')
            exit()
        print(tmp.content)
        print(1)


if __name__ == '__main__':
    obj = ipproxy()
    obj.check_ip()
    ip = obj.get_ip()
    print(ip)