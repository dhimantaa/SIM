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

        self._data = self._data[[(self._data['Date'] > datetime.datetime.strptime(startDate, '%Y%m%d')) &
                                 (self._data['Date'] < datetime.datetime.strptime(endDate, '%Y%m%d'))]]

        delta = self._data['Close'].diff()[1:]

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        if sma:
            # Calculate the SMA
            roll_up2 = pd.rolling_mean(up, window_length)
            roll_down2 = pd.rolling_mean(down.abs(), window_length)

            # Calculate the RSI based on SMA
            rsi_sma = roll_up2 / roll_down2
            return 100.0 - (100.0 / (1.0 + rsi_sma))
        else:
            # Calculate the EWMA

            roll_up1 = pd.stats.moments.ewma(up, window_length)
            roll_down1 = pd.stats.moments.ewma(down.abs(), window_length)

            # Calculate the RSI based on EWMA
            rsi_ewma = roll_up1 / roll_down1
            return 100.0 - (100.0 / (1.0 + rsi_ewma))
