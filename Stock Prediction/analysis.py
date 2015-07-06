#!/usr/bin/py
import pylab as plt
import numpy as np
import scipy.stats as stats
def readFile(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    result = {}
    for i in range(1, len(lines)):
        if lines[i][0].isalpha():
            l = lines[i].strip('\r\n').split(' ')
            data = np.asarray(map(float, l[1:]))
            result[l[0]] = data
    return result

def maxProfit(prices):
    profit = 0
    buy = 0
    sell = 0
    up = False
    down = False
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1] and not up:
            buy = i - 1;
            up = True;
            down = False;
        if prices[i] < prices[i - 1] and not down:
            sell = i - 1;
            up = False;
            down = True;
            profit += prices[sell] - prices[buy]
    if buy < len(prices) and up:
        sell = len(prices) - 1
        profit += prices[sell] - prices[buy]
    return profit

def main():
    filename = 'stock_sample.txt'
    samples = readFile(filename)
    for stock in samples:
        print stock
        print 'mean = ', np.mean(samples[stock])
        print 'std  = ', np.std(samples[stock])
        print 'var  = ', np.var(samples[stock])
        print 'max  = ', np.amax(samples[stock])
        print 'min  = ', np.amin(samples[stock])
        z, pval = stats.normaltest(samples[stock])
        if (pval < 0.05):
            print 'Not normal distribution'
        else:
            print 'Normal distribution'
        print 'max profit = ', maxProfit(samples[stock])
    """ plotting
    times = [x for x in range(1, 506)]
    plt.figure()
    plt.title('Stock chart')
    for stock in samples:
       plt.plot(times, sample[stock], label = stock)

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc = 'best')
    plt.show()
    """
main()

