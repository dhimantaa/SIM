"""
This module will download base data from quandl
"""

from api import Api


class Quandl(Api):

    def __init__(self, **kwargs):
        super(Quandl, self).__init__(**kwargs)