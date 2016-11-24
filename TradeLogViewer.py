"""Read the day's trading history"""
import pickle

trade_log = pickle.load(open('TradeLog.p','rb'))

print(trade_log)