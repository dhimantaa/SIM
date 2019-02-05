"""
This module will download base data from quandl
"""

import os
import json
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

    def bse_metadata(self):
        """

        :return:
        """
        self._url = source.BSE_META + '/metadata?api_key=' + source.QUANDL_API_KEY

        data = self._api.apply(False, url=self._url)
        zipfile.ZipFile(StringIO.StringIO(data[0])).extractall(os.path.join(os.path.dirname(__file__), 'meta'))

        if data[0]:
            return pd.read_csv(os.path.join(os.path.dirname(__file__), 'meta') + '/BSE_metadata.csv')
        else:
            raise BaseException

    def bse_id(self, symbol=None):
        """

        :param symbol:
        :return:
        """
        if symbol:
            self._url = source.BSE_ID + '/BSE/' + symbol + '/metadata'
            data = self._api.apply(False, url=self._url)

            if data[0]:
                return json.loads(data[0])['dataset']['id']
            else:
                return None
        else:
            return None

    def bse_data(self, bse_id=None):
        """

        :param bse_id:
        :return:
        """
        if bse_id:
            self._url = source.BSE_ID + '/' + str(bse_id) + '/data'
            data = self._api.apply(False, url=self._url)

            if data[0]:
                return data[0]
            else:
                return None
        else:
            return None

    def bse_instrument(self):
        """

        :return:
        """

        raise NotImplementedError
