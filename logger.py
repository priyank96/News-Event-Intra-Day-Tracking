''' Logs [Time, sell price, buy price] into TradeLog.csv''' 
import csv
import datetime

def logger(tradeLog):
    with open('TradeLog.csv','a') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            for i in tradeLog.keys():
                row = [datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),i]
                row.extend(tradeLog[i])
                writer.writerow(row)
        
    
