from headline_to_symbol import headline_to_symbol
from datetime import datetime, time
import csv
from closest_lines import closest_lines
from EntityClass import *
from plotter import plot, prepare_plots
import numpy as np
from time import sleep

entities = headline_to_symbol()
prepare_plots(entities)
num_entities = len(entities)
print(num_entities)
clock = datetime.now()
minutes = 0

while clock.time() < time(15, 30):
    clock = datetime.now()
    if clock.time() > time(9, 14):
        while datetime.now().second != 59:  # start at end of minute
            continue
        minutes += 1
        for i in range(0, num_entities):
            entities[i].update_values()
            with open(entities[i].file_name, 'r') as csvfile:
                line = []
                start = False
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:

                    if not start and row:
                        start = float(row[1])
                        line.append(0.0)
                    elif row:
                        # line.append(float(i + 1))
                        line.append((float(row[1]) - start) * 100 / start)

            similar_lines = list(map(lambda x: x[1], closest_lines(line, minutes)))
            while len(line) != len(similar_lines[0]):
                 line.append(np.nan)
            similar_lines.append(line)
            # print('here')
            plot(similar_lines, entities[i].id)

    else:
        print("waiting " + str(clock.time()))
    sleep(60)
