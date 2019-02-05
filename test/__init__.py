

import api


class Test:

    @staticmethod
    def run():
        api_object = api.Quandl()
        meta = api_object.bse_metadata('pandas')
        print meta.head()
        symbol = meta['code'].iloc[0]

        id = api_object.bse_id(symbol)['dataset/id'].iloc[0]

        print id

        return api_object.bse_data(bse_id=id)

