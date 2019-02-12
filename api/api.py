"""
This module will query free sources to collect the base data feed
"""

__author__ = "dhimantarun19@gmail.com"

import sys
import time
import requests


class Api(object):

    def __init__(self, source, **kwargs):
        """

        :param source:
        :param kwargs:
        """
        self.__url = source

    def _get(self, param=None, url=None, refresh_rate=None):
        """

        :type refresh_rate: this param should be in seconds
        :param param:
        :return:
        """
        try:
            if url:
                self.__url = url
            if refresh_rate:
                req = requests.get(self.__url)
                time.sleep(refresh_rate)
            else:
                req = requests.get(self.__url)
        except Exception as e:
            print (e)
            sys.exit()
        if req.status_code == 200:
            return req.content, req.status_code
        else:
            return None, req.status_code

    def _post(self, param=None, url=None, refresh_rate=None):
        """

        :type refresh_rate:
        :param param:
        :return:
        """
        data = {'api_key': param}
        if url:
            self.__url = url
        if refresh_rate:
            req = requests.post(self.__url, data)
            time.sleep(refresh_rate)
        else:
            req = requests.post(self.__url, data)
        if req.status_code == 200:
            return req.text, req.status_code
        else:
            return None, req.status_code

    def apply(self, func, param=None, url=None, refresh_rate=None):
        """

        :param refresh_rate:
        :param url:
        :param func:
        :param param:
        :return:
        """
        if func:
            return self._post(param=param, url=url,refresh_rate=refresh_rate)
        return self._get(param=param, url=url, refresh_rate=refresh_rate)

