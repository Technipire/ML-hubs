#!/usr/bin/py
import numpy as np
class stock:
    def __init__(self, name, prices, owned, action):
        self.name = name
        self.prices = prices
        self.num_owned = owned
        self.mean = np.mean(prices)
        self.std = np.std(prices)
        self.current_price = prices[len(prices) - 1]
        self.action = action.upper()
        self.current_max = np.amax(prices)
        self.current_min = np.amin(prices)
        self.priority = 0 # [0, 2] where 2 is the top priority


    def get_info(self):
        print
        print ' Stock name: ', self.name
        print '      Owned: ', self.num_owned
        print '       mean: ', self.mean
        print '        std: ', self.std
        print '  cur price: ', self.current_price
        print 'last action: ', self.action
        print
