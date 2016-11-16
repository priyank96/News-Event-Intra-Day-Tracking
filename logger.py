''' Logs [Time,  price, change price] into TradeLog.csv'''
import csv
import datetime


def logger(entity):
    row = [datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
    row.append(entity.priceList[-1])
    row.append(entity.prevDayDelta[-1])
    print(row)
    with open('TradeLog'+entity.ID+'.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row)
