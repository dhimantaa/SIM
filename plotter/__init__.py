"""
Plotter base class
"""

import numpy as np
import matplotlib.pyplot as plt


#from matplotlib import style
#style.use('fivethirtyeight')


class Plotter(object):

    def __init__(self, data=None, symbol=None, param=None):
        """

        :param data:
        :param symbol:
        :param param:
        """
        self._data = data
        self._symbol = symbol
        if not param:
            self._plot_param = {'fields': {'groups': [{'y': ['Close', 'rsi'], 'x': ['Date']},
                                                  {'y': ['No. of Shares'], 'x': ['Date']}]}}
        else:
            self._plot_param = param

    def plot(self):
        """

        :return:
        """
        group = self._plot_param['fields']['groups']
        plt_length = len(group)
        fig = plt.figure()
        plt.title(self._symbol)
        axis = {}
        prev_pos = 0
        for i in range(len(group)):

            if len(group[i]['y']) == 2:

                axis['ax_' + str(i)] = plt.subplot2grid((5 * plt_length, 1), (prev_pos, 0),
                                                        rowspan=5,
                                                        colspan=1)
                prev_pos += 5
                axis['ax_' + str(i)].set_ylabel(group[i]['y'][0])

                axis['ax_' + str(i)].plot(np.array(self._data[group[i]['x'][0]]),
                                          np.array(self._data[group[i]['y'][0]]))

                axis['ax_v' + str(i)] = axis['ax_' + str(i)].twinx()
                axis['ax_v' + str(i)].set_ylabel(group[i]['y'][1])

                axis['ax_v' + str(i)].plot(np.array(self._data[group[i]['x'][0]]),
                                           np.array(self._data[group[i]['y'][1]]))
                axis['ax_v' + str(i)].fill(facecolor='#0079a3')

            else:
                axis['ax_' + str(i)] = plt.subplot2grid((5 * plt_length, 1), (prev_pos+1, 0), rowspan=5, colspan=1)
                prev_pos += 5
                axis['ax_' + str(i)].set_ylabel(group[i]['y'][0])
                axis['ax_' + str(i)].plot(np.array(self._data[group[i]['x'][0]]),
                                          np.array(self._data[group[i]['y'][0]]))
