"""
This is base class for all indicators
"""

__author__ = 'dhimantarun19@gmail.com'

import proxy
import api
import feed


class Indicator(object):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self._symbol = kwargs['symbol']
        self._crawl = kwargs['db']

    def feed(self):
        """

        :return:
        """
        pass

    def simulation(self):
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
        pass
