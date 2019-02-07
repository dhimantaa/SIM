"""
This module to scrap different ip to set the proxy
"""

import lxml
import random
import urllib2
import cookielib
from bs4 import BeautifulSoup as bsm


def ip_crawler():
    """
    This function will crawl the ips to set proxy
    """
    proxy_site = 'https://free-proxy-list.net/'
    proxy_hdr = {'User-Agent': 'Mozilla/5.0'}
    global ips
    ips = []

    proxy_req = urllib2.Request(proxy_site, headers=proxy_hdr)
    proxy_url = urllib2.urlopen(proxy_req).read()

    rows = bsm(proxy_url, "lxml").findAll("tr")

    for row in rows:
        try:
            ip = [element.text for element in row.find_all('td')][0]
            if '.' in ip:
                ips.append(ip)
        except IndexError as e:
            pass


ip_crawler()


class Proxy(object):

    def __init__(self):
        """

        """
        self._block_list = []
        self._ip_index = 0

    def _proxy(self, browse_url=None, ip=None):
        """

        :param browse_url:
        :param url:
        :return:
        """
        hdr1 = {'User-Agent': 'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                # working Internet explorer 10 on version windows 3.1
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
                # Working #Internet Explorer 9 on Windows NT
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        hdr3 = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                # working #Internet Explorer 10 on Mac OS X (Lion)
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        hdr4 = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',  # working gooogle bot user agent
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        hdr5 = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; tr) Opera 10.10',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',  # working opera 10 on windows NT
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        hdr6 = {'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',  # working Microsoft bing bot useragent
                'Connection': 'keep-alive'}

        try:
            hdr = random.choice([hdr1, hdr2, hdr3, hdr4, hdr5, hdr6])
            req = urllib2.Request(browse_url, headers=hdr)

            cj = cookielib.CookieJar()
            proxy = urllib2.ProxyHandler({'http': ip})
            requested = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), proxy).open(req, timeout=10)
            return__code = requested.getcode()

            if return__code != 429:
                data = bsm(requested.read(), 'html.parser')
                data = data.findAll("code",
                                {"data-language": "ruby"})[0].text.strip().encode('ascii',
                                                                                  'replace').replace("?",
                                                                                                     " ")
            return data, return__code

        except:
            pass

    def use(self, browse_url=None):
        """

        :return:
        """

        if ips[self._ip_index] not in self._block_list:
            r = self._proxy(browse_url=browse_url, ip=ips[self._ip_index])
        else:
            ip_crawler()
            self._ip_index = 0

        if not r or r[1] == 429:
            self._block_list.append(ips[self._ip_index])
            self._ip_index += 1
            return self._proxy(browse_url=browse_url, ip=ips[self._ip_index])
        else:
            return r
