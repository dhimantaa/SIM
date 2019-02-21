"""
This is technical indicator
Bollinger bands
"""

__author__ = 'dhimantarun19@gmail.com'

import datetime
import pandas as pd
from Indicator import Indicator


class Bollinger(Indicator):

    def __init__(self, **kwargs):
        super(Bollinger, self).__init__(**kwargs)
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

        # Calculating the 20-day SMA
        self._data['sma_20'] = self._data['Close'].rolling(window=20, center=False).mean()

        # Calculating the 20-day std
        self._data['std_20'] = self._data['Close'].rolling(window=20).std()

        # Calculating the Upper band of bollinger band
        self._data['upper_band'] = self._data['sma_20'] + 2*self._data['std_20']

        # Calculating the Lower band of bollinger band
        self._data['lower_band'] = self._data['sma_20'] - 2 * self._data['std_20']

        param = {'fields': {'groups': [{'y': [['Close', 'sma_20', 'upper_band', 'lower_band']], 'x': ['Date']},
                                       {'y': ['No. of Shares'], 'x': ['Date']}]}}

        if startDate and endDate:
            self._data = self._data[(self._data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                                    (self._data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]
        else:
            self._data = self._data[(self._data['Date'] > datetime.datetime(2010, 1, 1)) &
                                    (self._data['Date'] < datetime.datetime(2012, 1, 1))]

        return self._data, param
