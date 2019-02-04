"""
This module will query free sources to collect the base data feed
"""
import sys
import requests


class Api(object):

    def __init__(self, source, **kwargs):
        """

        :param source:
        :param kwargs:
        """
        self.__url = source

    def _get(self, param=None, url=None):
        """

        :param param:
        :return:
        """
        try:
            if url:
                self.__url = url

            req = requests.get(self.__url)
        except Exception as e:
            print (e)
            sys.exit()

        if req.status_code == 200:
            return req.content, req.status_code
        else:
            return None, req.status_code

    def _post(self, param=None, url=None):
        """

        :param param:
        :return:
        """
        data = {'api_key': param}
        if url:
            self.__url = url

        req = requests.post(self.__url, data)
        if req.status_code == 200:
            return req.text, req.status_code
        else:
            return None, req.status_code

    def apply(self, func, param=None, url=None):
        """

        :param url:
        :param func:
        :param param:
        :return:
        """
        if func:
            return self._post(param=param, url=url)
        return self._get(param=param, url=url)

