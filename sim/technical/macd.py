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

        # Calculating 12 day Exponential moving average for the base line
        data['ema_12'] = self.ema(window_size=12, name='Close')

        # Calculating 26 day Exponential moving average for the base line
        data['ema_26'] = self.ema(window_size=26, name='Close')

        # Calculating macd
        data['macd'] = data['ema_12'] - data['ema_26']

        # Calculating 9 day moving average for the single line
        data['sma_9'] = self.sma(window_size=9, name='Close')

        param = {'fields': {'groups': [{'y': ['Close'], 'x': ['Date']},
                                       {'y': ['sma_9', 'macd'], 'x': ['Date']},
                                       {'y': ['No. of Shares'], 'x': ['Date']}]}}

        if startDate and endDate:
            data = data[(data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                        (data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]
        else:
            data = data[(data['Date'] > datetime.datetime(2010, 1, 1)) &
                        (data['Date'] < datetime.datetime(2012, 1, 1))]

        return data, param
