'''Accept array of entities, log headlines and price data'''
import EntityClass
import numpy as np
import pandas as pd
import os.path
import datetime

def log_data(entities):
    today = str(datetime.date.today())
    file_name = EntityClass.past_trades_file_name
    if os.path.isfile(file_name):
        past_trades_hl = pd.read_hdf(file_name, key='headline')
        fresh_trades_hl = pd.DataFrame()
        for entity in entities:
            fresh_trades_hl[entity.headline] = entity.line
        past_trades_hl = pd.concat([past_trades_hl, fresh_trades_hl], ignore_index=True, axis=1)

        past_trades_date = pd.read_hdf(file_name, key='date')
        fresh_trades_date = pd.DataFrame()
        for entity in entities:
            fresh_trades_date[entity.headline] = entity.line
        past_trades_date = pd.concat([past_trades_date, fresh_trades_date], ignore_index=True, axis=1)

    else:
        past_trades_hl = pd.DataFrame()
        for entity in entities:
            past_trades_hl[entity.headline] = entity.line
        past_trades_date = pd.DataFrame()

        for x, entity in enumerate(entities):
            past_trades_hl[today+" "+str(x)] = entity.line  # unique column headings are ensured

    hdf = pd.HDFStore(file_name)
    hdf.put('headline', past_trades_hl, data_columns=True)
    hdf.put('date', past_trades_date, data_columns = True)
    print(past_trades_date.shape)

if __name__ == '__main__':
    past_trades = pd.read_hdf('PastTrades.h5', key='PastTrades')
    print(past_trades)
