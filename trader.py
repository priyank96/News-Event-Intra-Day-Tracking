from headline_to_symbol import headline_to_symbol
from datetime import datetime, time
from closest_lines import closest_lines
from plotter import plot, prepare_plots
from data_logger import log_data
from time import sleep
from EntityClass import EntityClass
import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB

# readying entities
entities = headline_to_symbol()
ans = str(input("Add entity? (y/n)"))
while ans == 'y':
    symbol = str(input("Enter symbol:"))
    headline = str(input("Enter headline:"))
    entities.append(EntityClass(symbol, headline))
    ans = str(input("Add entity? (y/n)"))
prepare_plots(entities)
num_entities = len(entities)

# readying stored data
data_fil = 'PastTrades.h5'
data = pd.read_hdf(data_fil, key='date')  # dataframe of past prices
output_fil = 'outputs.p'
outputs = pickle.load(open(output_fil, 'rb'))  # dict of outputs
print("Done- data load")

minutes = -1
clock = datetime.now()

while clock.time() < time(15, 30):
    clock = datetime.now()
    if clock.time() > time(9, 14):
        minutes += 1
        try:
            if 0 < minutes < 90:  # largest index before NaN values appear in data
                print("Start- classifier training")
                ip = []
                op = []
                for column in data:
                    ip.append(data[column][:minutes+1])
                    op.append(outputs[column][minutes+1])
                classifier = GaussianNB()
                classifier.fit(ip, op)
                print("Done- classifier training")
        except Exception as e:
            print(str(e))

        while datetime.now().second != 59:  # start at end of minute
            continue


        for entity in entities:
            entity.update_values()
            # similar_lines = list(map(lambda x: x[1], closest_lines(entity.line, minutes)))
            # similar_lines = []
            # similar_lines.append(entity.line)

            plot(entity.line, entity.id)
            try:
                if 0 < minutes < 90:  # largest index before NaN values appear in data
                    print(entity.id)
                    print(classifier.predict(entity.line))
            except Exception as e:
                print(str(e))
    else:
        print("waiting " + str(clock.time()))
    sleep(60)
log_data(entities)
