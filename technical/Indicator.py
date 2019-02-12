"""
This is base class for all indicators
"""

__author__ = 'dhimantarun19@gmail.com'

import os
import json


class Indicator(object):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self._symbol = kwargs['symbol']
        self._crawl = kwargs['db']
        self._data_type = kwargs['dtype']

    def feed(self):
        """

        :return:
        """
        if self._crawl:
            pass
        else:
            if self._data_type == 'json':
                file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                         'api', 'data', 'json', self._symbol)
            else:
                file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                         'api', 'data', 'json', self._symbol)

            return json.loads(open(file_path, 'r').read())

    def simulation(self, plot=None):
        """
        This method will have all the logic
        for the corresponding technical indicators
        :return:
        """
        raise NotImplementedError

    def run(self):
        """

        :return:
        """
        self.simulation(plot=True)
