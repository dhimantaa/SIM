"""
This module will query free sources to collect the base data feed
"""
import sys
import requests


class Api(object):

    def __init__(self, source, **kwargs):
        """

        :param source:
        :param instrument:
        """
        self.__url = source
        self.__instrument = kwargs['instrument']

    def _get(self, param=None):
        """

        :param param:
        :return:
        """
        try:
            if param:
                pass
            else:
                req = requests.get(self.__url+'/'+self.__instrument+'.csv')
        except Exception as e:
            print (e)
            sys.exit()

        if req.status_code == 200:
            return req.text, req.status_code
        else:
            return None, req.status_code

    def _post(self, param=None):
        """

        :param param:
        :return:
        """
        raise NotImplementedError
