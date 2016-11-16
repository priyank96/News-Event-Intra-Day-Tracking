"""Class encapsulating stock details and methods"""
from __future__ import division

from BSEQuote import getPrice


class Entity:
    def __init__(self, ID):
        self.ID = ID  # Security code
        self.priceList = []  # List of prices
        self.movingAvg = []  # List of moving averages
        self.cornerPoint = 1  # Diff. b/w last moving-avg. and current moving-avg.
        self.holdState = 0  # -1:Sold, 0: Not Held,1: Bought, Done Trading
        self.prevDayDelta = []
        self.trade = []  # price of buy/sell

    def Avg(self):  # exponential moving average for 10 period
        if (len(self.priceList) == 1):
            self.movingAvg.append(self.priceList[-1])
        else:
            self.movingAvg.append((self.priceList[-1] * 0.1818) + (self.movingAvg[-1] * 0.8181))

    def updateValues(self, mode='real'):
        quote = getPrice(self.ID, mode)
        self.priceList.append(quote[1])  # prices updated

        self.Avg()

        if len(self.movingAvg) > 2:
            self.cornerPoint = self.movingAvg[-1] - self.movingAvg[-2]  # corner updated

        self.prevDayDelta.append(quote[2])
    

    def __repr__(self):
        return str(self.trade)  

    def __str__(self):
        if (len(self.movingAvg) > 0):
            return self.ID + "  " + str(self.priceList[-1]) + " Moving average: " + str(self.movingAvg[-1])
        else:
            return self.ID + "  " + str(self.priceList[-1])
