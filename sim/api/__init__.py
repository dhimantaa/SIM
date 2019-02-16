"""
This module will download base data from quandl
"""

__author__ = 'dhimantarun19@gmail.com'

import os
import sys
import json
import source
import zipfile
import StringIO
import warnings
import collections
from api import Api
import pandas as pd
from ..proxy import Proxy


class Quandl:

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self._url = source.QUANDL
        self._api = Api(self._url)
        if kwargs.keys():
            self._proxy = kwargs['proxy']
            self.symbol = kwargs['symbol']
        else:
            warnings.warn('Empty argument given')
            self._proxy = True
            self.symbol = 'BOM500002'

        if self._proxy:
            self._p = Proxy()

    def bse_metadata(self, format=None):
        """

        :param format:
        :return:
        """
        self._url = source.BSE_META + '/metadata?api_key=' + source.QUANDL_API_KEY

        data = self._api.apply(False, url=self._url)
        zipfile.ZipFile(StringIO.StringIO(data[0])).extractall(os.path.join(os.path.dirname(__file__), 'meta'))

        if data[0]:
            if format == 'pandas':
                return pd.read_csv(os.path.join(os.path.dirname(__file__), 'meta') + '/BSE_metadata.csv')
            else:
                return 'Saved under meta'
        else:
            raise BaseException

    def bse_id(self, symbol=None):
        """

        :param symbol:
        :return:
        """
        if symbol:
            self._url = source.BSE_ID + '/BSE/' + symbol + '/metadata'
            if self._proxy:
                data = self._p.use(self._url)
            else:
                data = self._api.apply(False, url=self._url)

            if data[1] == 200:
                return self._convert_to_dd(json.loads(data[0]))
            elif data[1] == 404:
                warnings.warn(str(data[0]) + ' : ' + symbol)
                sys.exit()
            else:
                return None
        else:
            return None

    def bse_data(self, bse_id=None, refresh_rate=None, format='json'):
        """

        :param format:
        :param refresh_rate:
        :param bse_id:
        :return:
        """
        if bse_id:
            self._url = source.BSE_ID + '/' + str(bse_id) + '/data'
            if self._proxy:
                data = self._p.use(self._url)
            else:
                data = self._api.apply(False, url=self._url, refresh_rate=refresh_rate)

            if data[1] == 200:
                if format == 'json':
                    return json.loads(data[0])
                else:
                    return self._convert_to_dd(json.loads(data[0]))
            elif data[1] == 404:
                warnings.warn(str(data[0]) + ' : ' + bse_id)
                sys.exit()
            else:
                return None
        else:
            return None

    def save_data(self, refresh=False, refresh_symbol=False, refresh_rate=None, format='json', single=False):
        """

        :param single:
        :param format:
        :param refresh_rate:
        :param refresh_symbol:
        :param refresh:
        :return:
        """
        if refresh:
            df = self.bse_metadata('pandas')
            symbol_list = df['code']
        elif single:
            symbol_list = [self.symbol]
        else:
            df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'meta') + '/BSE_metadata.csv')
            symbol_list = df['code']

        for symbol in symbol_list:
            print symbol
            if os.path.isfile(os.path.join(os.path.dirname(__file__),
                                           'data') + '/' + format + '/' + symbol) and not refresh_symbol:

                print ('Data already saved for {}'.format(symbol))
            else:
                try:
                    bse_id = self.bse_id(symbol=symbol)['dataset/id'].iloc[0]
                    data = self.bse_data(bse_id=bse_id, refresh_rate=refresh_rate, format=format)

                    if isinstance(data, pd.DataFrame):

                        data.to_csv(os.path.join(os.path.dirname(__file__), 'data') + '/csv/' + symbol)
                        print ('Saved data for {}'.format(symbol))
                    elif format == 'json':

                        with open(os.path.join(os.path.dirname(__file__), 'data') + '/json/' + symbol,
                                  'w') as outfile:
                            json.dump(data, outfile)
                    else:
                        print ('No data found for {}'.format(symbol))

                except Exception as e:
                    print e
                    pass

    def save_tmp(self):
        """
        This function will crawl data in the production
        :return: The data in json object
        """
        bse_id = self.bse_id(symbol=self.symbol)['dataset/id'].iloc[0]
        return self.bse_data(bse_id=bse_id, refresh_rate=None, format='json')

    def _convert_to_dd(self, data):
        """

        :param data:
        :return:
        """
        output = collections.defaultdict(list)
        for op in self._json_parser(indict=data):
            output['/'.join(op[:-1])].append(op[-1])

        pandas_data = pd.DataFrame()

        for key in output.keys():
            pandas_data[key] = pd.Series(output[key])

        return pandas_data

    def _json_parser(self, indict=None, pre=None):
        """

        :param indict:
        :param pre:
        :return:
        """

        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    for d in self._json_parser(value, pre + [key]):
                        yield d
                elif isinstance(value, list) or isinstance(value, tuple):
                    i = 0
                    for v in value:
                        if not (isinstance(v, list) or isinstance(v, dict) or isinstance(v, tuple)):
                            yield pre + [key, v]
                        else:
                            for d in self._json_parser(v, pre + [key]):
                                yield d
                        i += 1
                else:
                    yield pre + [key, value]
        else:
            yield pre + [indict]

    def bse_instrument(self):
        """

        :return:
        """

        raise NotImplementedError
