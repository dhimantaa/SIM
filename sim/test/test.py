__author__ = 'dhimantarun19@gmail.com'

import unittest
import datetime
from sim.technical import macd
from sim.technical import rsi
from sim.technical import bollinger


class TechnicalTest(unittest.TestCase):

    def test_bollinger(self):
        """

        :return:
        """
        self._symbol = 'BOM500003'
        self._startDate = '20100101'
        self._endDate = '20120101'
        out = bollinger.Bollinger(symbol=self._symbol).simulation(startDate=self._startDate,
                                                                  endDate=self._endDate)
        self.assertFalse(out[0].empty)

    def test_macd(self):
        """

        :return:
        """
        self._symbol = 'BOM500003'
        self._startDate = '20100101'
        self._endDate = '20120101'
        out = macd.Macd(symbol=self._symbol).simulation(startDate=self._startDate,
                                                        endDate=self._endDate)

        self.assertFalse(out[0].empty)

    def test_rsi(self):
        """

        :return:
        """
        self._symbol = 'BOM500003'
        self._startDate = '20100101'
        self._endDate = '20120101'
        out = rsi.Rsi(symbol=self._symbol).simulation(startDate=self._startDate,
                                                      endDate=self._endDate)

        self.assertFalse(out[0].empty)


if __name__ == '__main__':
    unittest.main()
