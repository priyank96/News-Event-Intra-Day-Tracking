'''Accept array of entities, log headlines and price data'''
import EntityClass
import numpy as np
import pandas as pd
import os.path
import datetime

str_of_date = str(datetime.date.today())


def log_data(entities):
    file_name = EntityClass.past_trades_file_name
    if os.path.isfile(file_name):
        past_trades_date = pd.read_hdf(file_name, key='date')
        fresh_trades_date = pd.DataFrame()
        for entity in entities:
            fresh_trades_date[entity.headline + ' ' + str_of_date] = entity.line
        past_trades_date = pd.concat([past_trades_date, fresh_trades_date], axis=1)

    hdf = pd.HDFStore(file_name)

    hdf.put('date', past_trades_date, data_columns=True)
    print(past_trades_date.shape)


if __name__ == '__main__':

    try:
        past_trades = pd.read_hdf('PastTrades.h5', key='date')
        print(past_trades.columns.values)


    except KeyError as e:
        print(e)
