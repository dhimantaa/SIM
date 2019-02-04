"""
This module will download base data from quandl
"""

import os
import source
import zipfile
import StringIO
from api import Api
import pandas as pd


class Quandl:

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self._url = source.QUANDL
        self._api = Api(self._url)
        self.symbol = kwargs['symbol']

    def bse_metadata(self):
        """

        :return:
        """
        self._url = source.BSE + '/metadata?api_key=' + source.QUANDL_API_KEY

        data = self._api.apply(False, url=self._url)
        zipfile.ZipFile(StringIO.StringIO(data[0])).extractall(os.path.join(os.path.dirname(__file__), 'tmp'))

        if data[0]:
            return pd.read_csv(os.path.join(os.path.dirname(__file__), 'tmp') + '/BSE_metadata.csv')
        else:
            raise BaseException

    def bse_data(self):
        """

        :return:
        """
        raise NotImplementedError

    def bse_instrument(self):
        """

        :return:
        """

        raise NotImplementedError
