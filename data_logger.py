'''Accept array of entities, log headlines and price data'''
import EntityClass
import numpy as np
import pandas as pd
import os.path


def log_data(entities):
    file_name = EntityClass.past_trades_file_name
    if os.path.isfile(file_name):
        past_trades = pd.read_hdf(file_name, key='PastTrades')
        fresh_trades = pd.DataFrame()
        for entity in entities:
            fresh_trades[entity.headline] = entity.line
        past_trades = pd.concat([past_trades, fresh_trades], ignore_index=True, axis=1)
    else:
        past_trades = pd.DataFrame()
        for entity in entities:
            past_trades[entity.headline] = entity.line
    hdf = pd.HDFStore(file_name)
    hdf.put('PastTrades', past_trades, data_columns=True)
    print(past_trades.shape)

if __name__ == '__main__':
    past_trades = pd.read_hdf('PastTrades.h5', key='PastTrades')
    print(past_trades)
