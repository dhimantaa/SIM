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

    def simulation(self, plot=None, startDate=None, endDate=None):
        """

        :param plot:
        :param startDate:
        :param endDate:
        :return:
        """

        # Calculating the 20-day SMA
        data['sma_20'] = self.sma(window_size=20, name='Close')

        # Calculating the 20-day std
        data['std_20'] = self.std(window_size=20, name='Close')

        # Calculating the Upper band of bollinger band
        data['upper_band'] = data['sma_20'] + 2*data['std_20']

        # Calculating the Lower band of bollinger band
        data['lower_band'] = data['sma_20'] - 2 * data['std_20']

        param = {'fields': {'groups': [{'y': [['Close', 'sma_20', 'upper_band', 'lower_band']], 'x': ['Date']},
                                       {'y': ['No. of Shares'], 'x': ['Date']}]}}

        if startDate and endDate:
            data = data[(data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                        (data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]
        else:
            data = data[(data['Date'] > datetime.datetime(2010, 1, 1)) &
                        (data['Date'] < datetime.datetime(2012, 1, 1))]

        return data, param
