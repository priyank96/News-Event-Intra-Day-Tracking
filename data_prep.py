import pandas as pd
import pickle
from plotter import plot, prepare_plots
from EntityClass import EntityClass

fil = 'PastTrades.h5'
minutes = 91  # largest time before NaNs appear

data = pd.read_hdf(fil, key='date')
print(pickle.load(open("outputs.p", "rb")))

try:
    times = pickle.load(open("outputs.p", "rb"))
except:
    times = dict()


prepare_plots([EntityClass('temp')])
for column in data:
    if column not in times.keys():
        plot(list(data[column][:minutes]), 'temp')
        sell = int(input("enter sell time:"))
        if sell == -1:
            times[column] = [0] * minutes
            continue
        buy = int(input("enter buy time:"))
    
        times[column] = [0] * minutes
        times[column][sell] = -1
        times[column][buy] = 1
pickle.dump(times, open("outputs.p", "wb"))
