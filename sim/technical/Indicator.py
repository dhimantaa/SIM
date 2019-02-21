"""
This is base class for all indicators
"""

__author__ = 'dhimantarun19@gmail.com'

import os
import json
import pandas as pd
from ..api import Quandl


def _sma(window_size=None, data=None, name=None):
    """

    :param window_size:
    :param name:
    :return:
    """

    if window_size and name:
        data['sma_' + str(window_size)] = data[name].rolling(window=window_size).mean()
        return data
    else:
        return data['Close'].rolling(window=window_size).mean()


def _ema(window_size=None, data=None, name=None):
    """

    :param window_size:
    :param name:
    :return:
    """

    if window_size and name:
        return data[name].ewm(ignore_na=False,
                              min_periods=0,
                              adjust=True,
                              com=window_size).mean()
    else:
        return data['Close'].ewm(ignore_na=False,
                                 min_periods=0,
                                 adjust=True,
                                 com=window_size).mean()


def _std(window_size=None, data=None, name=None):
    """

    :param window_size:
    :param name:
    :return:
    """

    if window_size and name:
        return data[name].rolling(window=window_size).std()
    else:
        return data['Close'].rolling(window=window_size).std()


class Indicator(object):

    def __init__(self, symbol='BOM500002', db=None, datatype='json', proxy=True, prod=True):
        """

        :type prod:
        :param symbol:
        :param db:
        :param datatype:
        """
        self._symbol = symbol
        self._crawl = db
        self._data_type = datatype
        self._proxy = proxy
        self._prod = prod

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

                if not os.path.isfile(file_path):
                    # download data from the source
                    if self._prod:
                        return Quandl(symbol=self._symbol, proxy=self._proxy).save_tmp()
                    else:
                        Quandl(symbol=self._symbol, proxy=self._proxy).save_data(single=True)
            else:
                file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                         'api', 'data', 'json', self._symbol)
                if not os.path.isfile(file_path):
                    # download data from the source
                    if self._prod:
                        return Quandl(symbol=self._symbol, proxy=self._proxy).save_tmp()
                    else:
                        Quandl(symbol=self._symbol, proxy=self._proxy).save_data(single=True)

            return json.loads(open(file_path, 'r').read())

    def sma(self, window_size=None, name=None):
        """

        :param window_size:
        :param name:
        :return:
        """

        data = pd.DataFrame(data=self.feed()["dataset_data"]["data"],
                            columns=self.feed()["dataset_data"]["column_names"])

        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

        data = data.sort_values(by=['Date'])

        return _sma(window_size=window_size, data=data, name=name)

    def ema(self, window_size=None, name=None):
        """

        :param window_size:
        :param name:
        :return:
        """

        data = pd.DataFrame(data=self.feed()["dataset_data"]["data"],
                            columns=self.feed()["dataset_data"]["column_names"])

        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

        data = data.sort_values(by=['Date'])

        return _ema(window_size=window_size, data=data, name=name)

    def std(self, window_size=None, name=None):
        """

        :param window_size:
        :param name:
        :return:
        """

        data = pd.DataFrame(data=self.feed()["dataset_data"]["data"],
                            columns=self.feed()["dataset_data"]["column_names"])

        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

        data = data.sort_values(by=['Date'])

        return _std(window_size=window_size, data=data, name=name)

    def simulation(self, plot=None):
        """
        This method will have all the logic
        for the corresponding technical indicators
        :return:
        """
        raise NotImplementedError

