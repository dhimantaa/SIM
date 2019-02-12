"""
This is base class for all indicators
"""

__author__ = 'dhimantarun19@gmail.com'

import os
import json


class Indicator(object):

    def __init__(self, symbol='BOM500002', db=None, datatype='json'):
        """

        :param symbol:
        :param db:
        :param datatype:
        """
        self._symbol = symbol
        self._crawl = db
        self._data_type = datatype

    def feed(self):
        """

        :return:
        """
        if self._crawl:
            """
            !! Under construction !!
            """
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

    def strategy(self):
        """

        :return:
        """
        raise NotImplementedError

    def run(self):
        """

        :return:
        """
        self.simulation(plot=True)
