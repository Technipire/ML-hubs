#!/usr/bin/py
import pylab as plt
import numpy as np
import math
import scipy.stats as stats
from stock import stock

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

def method1():
    filename = 'sample.txt'
    infile = open(filename, 'r')
    lines = infile.readlines()
    l = lines[0].strip('\r\n').split()
    m = int(l[0]) # amount of money
    k = int(l[1]) # number of different stocks
    d = int(l[2]) # number of remaining days
    data = readFile(filename)
    stock_list = []
    for stock_name in data:
        newStock = stock(stock_name, map(float,data[stock_name][1:]), int(data[stock_name][0]), 'NONE')
        stock_list.append(newStock)

    stock_list = analyze_stock_list(stock_list)

def sell_stocks(stock_list):
    if len(stock_list) == 0: return 0
    for stk in stock_list:
        if stk.action == 'SELL':
            amount = stk.current_price * stk.num_owned
            stk.num_owned = 0
    return amount, stock_list

def buy_stocks(stock_list, money_onhand):
    """
    Purpose: takes the money on hand and updated stock list and buy the stocks 
    that are labelled as 'BUY', according to priorities

    Return: the updated stock_list and amount of money left after buying
    the stocks

    Issue: always use all the money on hand to buy the stock with top priority
    """
    if len(stock_list) == 0: return 0
    stock_list.sort(key = lambda x : x.priority, reverse = True)
    for stk in stock_list:
        if stk.action == "BUY":
            if stk.current_price <= money_onhand:
                nums = math.floor(money_onhand / current_price)
                money_onhand -= stk.current_price * nums
                stk.num_owned += num

    return money_onhand, stock_list

def make_transactions(stock_list, m, k):
    """
    Purpose: carry out transactions until no days left
    Return: final amount and stock_list
    """
    days = 0
    while days < k:
        amount_earned, stock_list = sell_stocks(stock_list)
        if (days == k - 1):
            m += amount_earned
            return m
        # I cannot spend amount_earned until the next day
        m, stock_list = buy_stocks(stock_list, m)
        days += 1
        m += amount_earned
    
    return mi, stock_list

def analyze_stock_list(stock_list):
    """
    Purpose: analyze the stock lists and assign a prelimilary BUY or SELL to each stock
    as well as priorities of actions

    Return: updated stock_list
    """
    if len(stock_list) == 0: return []
    for stk in stock_list:
        if (stk.current_price >= stk.mean + stk.std or stk.current_price >= 2 * stk.mean)\
           and stk.num_owned > 0:
            stk.action = 'SELL'
            if (stk.current_price >= stk.mean + 2 * stk.std)\
                    or stk.current_price == stk.current_max:
                stk.priority = 2
            else:
                stk.priority = 1
        elif (stk.current_price <= stk.mean - stk.std) \
                    or (stk.current_price <= stk.mean / 2.0):
            stk.action = 'BUY'
            if stk.current_price <= stk.mean - 2 * stk.std \
                    or stk.current_price == stk.current_min:
                stk.priority = 2
            else:
                stk.priority = 1
        else:
            stk.action = 'NONE'

    return stock_list

def main():
    filename = 'stock_sample.txt'
    samples = readFile(filename)
    for stock_name in samples:
        print stock_name
        print 'mean = ', np.mean(samples[stock_name])
        print 'std  = ', np.std(samples[stock_name])
        print 'var  = ', np.var(samples[stock_name])
        print 'max  = ', np.amax(samples[stock_name])
        print 'min  = ', np.amin(samples[stock_name])
        z, pval = stats.normaltest(samples[stock_name])
        if (pval < 0.05):
            print 'Not normal distribution'
        else:
            print 'Normal distribution'
            print 'max profit = ', maxProfit(samples[stock_name])
    
    method1()
    """ plotting
    times = [x for x in range(1, 506)]
    plt.figure()
    plt.title('stock chart')
    for stock_name in samples:
       plt.plot(times, sample[stock_name], label = stock)

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc = 'best')
    plt.show()
    """
main()

