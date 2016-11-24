""" Simulates trading, logs trading action in tradeLog.p"""

# from __future__ import division
from time import sleep
from datetime import datetime, time

import pickle
import headline_to_symbol as hs



def tradeWith(entity):
    entity.updateValues()
    if entity.holdState == 1:
        return 1  # done trading, running for price history
    if entity.cornerPoint < 0 and entity.holdState == 0 and entity.prevDayDelta[-1] > 0:  # Sell
        entity.holdState = -1
        entity.trade.append(entity.priceList[-1])
        print(entity.trade[0])

    if entity.holdState == -1 and ((entity.trade[0] - entity.priceList[-1]) / entity.priceList[-1]) > 0.0039:  # Buy
        entity.holdState = 1
        entity.trade.append(entity.priceList[-1])
        print((entity.trade[0] - entity.priceList[-1]) / entity.priceList[-1])


    return -1  # not done trading, don't get rid of entity


if __name__ == "__main__":

    entities = hs.headline_to_symbol()  # stocks to trade on the Bombay Stock Exchange

    while datetime.now().second != 59:  # start at end of minute
        continue

    tradeLog = {entity.ID: [] for entity in entities}

    while datetime.now().time() < time(15, 30):
        if datetime.now().time() > time(9, 14):
            for entity in entities:
                if tradeWith(entity) == 1:  # done trading

                    tradeLog[entity.ID] = entity.trade
                    entity.log()
                    #entities.remove(entity)
                    continue

                else:

                    tradeLog[entity.ID] = entity.trade
                    entity.log()

        else:
            print("waiting " + str(datetime.now().time()))

        with open('TradeLog.p', 'wb') as fil:
            pickle.dump(tradeLog, fil)
        sleep(60)
        # if i.holdState == 1 and i.cornerPoint>0:
        #    i.holdState = 2
        #    i.trade.append(i.priceList[-1])
        #    print (i.trade[1])
        #    tradeLog[i.ID].append(i.priceList[-1])


        # if i.holdState == 2  and i.cornerPoint<0 and ((i.priceList[-1]-i.trade[1])/i.trade[1])>0.0030 :
        #    i.holdState = 5
        #    tradeLog[i.ID].append(i.priceList[-1])

    print("Done- trader")
