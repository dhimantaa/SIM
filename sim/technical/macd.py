"""
This is technical indicator
Moving Average convergence divergence
"""

__author__ = 'dhimantarun19@gmail.com'

import datetime
import pandas as pd
from Indicator import Indicator


class Macd(Indicator):

    def __init__(self, **kwargs):
        super(Macd, self).__init__(**kwargs)
        self._data = pd.DataFrame(data=self.feed()["dataset_data"]["data"],
                                  columns=self.feed()["dataset_data"]["column_names"])

    def simulation(self, plot=None, startDate=None, endDate=None):
        """

        :param plot:
        :param startDate:
        :param endDate:
        :return:
        """

        self._data['Date'] = pd.to_datetime(self._data['Date'], format='%Y-%m-%d')

        self._data = self._data.sort_values(by=['Date'])

        # Calculating 12 day Exponential moving average for the base line
        self._data['ema_12'] = self._data['Close'].ewm(ignore_na=False,
                                                       min_periods=0,
                                                       adjust=True,
                                                       com=12).mean()
        # self._data['ema_12'] = pd.stats.moments.ewma(self._data['Close'], 12)

        # Calculating 26 day Exponential moving average for the base line
        self._data['ema_26'] = self._data['Close'].ewm(ignore_na=False,
                                                       min_periods=0,
                                                       adjust=True,
                                                       com=26).mean()
        # self._data['ema_26'] = pd.stats.moments.ewma(self._data['Close'], 26)

        # Calculating macd
        self._data['macd'] = self._data['ema_12'] - self._data['ema_26']

        # Calculating 9 day moving average for the single line
        self._data['sma_9'] = self._data['macd'].rolling(window=9, center=False).mean()

        param = {'fields': {'groups': [{'y': ['Close'], 'x': ['Date']},
                                       {'y': ['sma_9', 'macd'], 'x': ['Date']},
                                       {'y': ['No. of Shares'], 'x': ['Date']}]}}

        if startDate and endDate:
            self._data = self._data[(self._data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                                    (self._data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]
        else:
            self._data = self._data[(self._data['Date'] > datetime.datetime(2010, 1, 1)) &
                                    (self._data['Date'] < datetime.datetime(2012, 1, 1))]

        return self._data, param
