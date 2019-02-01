"""
This module will download base data from quandl
"""

import source
from api import Api


class Quandl(Api):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(Quandl, self).__init__(source.QUANDL, **kwargs)
        pass
