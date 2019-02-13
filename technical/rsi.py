"""
This is technical indicator
Relative strength index
"""

__author__ = 'dhimantarun19@gmail.com'

import datetime
import pandas as pd
from Indicator import Indicator


class Rsi(Indicator):

    def __init__(self, **kwargs):
        super(Rsi, self).__init__(**kwargs)
        self._data = pd.DataFrame(data=self.feed()[0]["dataset_data"]["data"],
                                  columns=self.feed()[0]["dataset_data"]["column_names"])

    def simulation(self, plot=None, startDate=None, endDate=None, window_length=14, sma=False):
        """

        :param sma:
        :param window_length:
        :param plot:
        :param startDate:
        :param endDate:
        :return:
        """

        self._data['Date'] = pd.to_datetime(self._data['Date'], format='%Y-%m-%d')

        if startDate and endDate:
            self._data = self._data[(self._data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                                    (self._data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]
            print self._data
        else:
            self._data = self._data[(self._data['Date'] > datetime.datetime(2010, 1, 1)) &
                                    (self._data['Date'] < datetime.datetime(2012, 1, 1))]

        positive, negative = self._data['Close'].diff()[1:].copy(), self._data['Close'].diff()[1:].copy()
        positive[positive < 0] = 0
        negative[negative > 0] = 0

        if sma:
            # Calculate the SMA
            roll_up2 = positive.rolling(window=9, center=False).mean()
            roll_down2 = negative.abs().rolling(window=9, center=False).mean()

            # roll_up2 = pd.rolling_mean(positive, window_length)
            # roll_down2 = pd.rolling_mean(negative.abs(), window_length)

            # Calculate the RSI based on SMA
            rs = roll_up2 / roll_down2
            self._data['rsi'] = 100.0 - (100.0 / (1.0 + rs))
            return self._data
        else:
            # Calculate the EWMA
            roll_up1 = positive.ewm(ignore_na=False,
                                    min_periods=0,
                                    adjust=True,
                                    com=window_length).mean()
            roll_down1 = negative.abs().ewm(ignore_na=False,
                                            min_periods=0,
                                            adjust=True,
                                            com=26).mean()

            # roll_up1 = pd.stats.moments.ewma(positive, window_length)
            # roll_down1 = pd.stats.moments.ewma(negative.abs(), window_length)

            # Calculate the RSI based on EWMA
            rs = roll_up1 / roll_down1
            self._data['rsi'] = 100.0 - (100.0 / (1.0 + rs))
            param = {'fields': {'groups': [{'y': ['Close', 'rsi'], 'x': ['Date']},
                                           {'y': ['No. of Shares'], 'x': ['Date']}]}}
            return self._data, param
