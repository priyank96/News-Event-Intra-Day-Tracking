from headline_to_symbol import headline_to_symbol
from datetime import datetime, time
from closest_lines import closest_lines
from plotter import plot, prepare_plots
from data_logger import log_data
from time import sleep

entities = headline_to_symbol()
prepare_plots(entities)
num_entities = len(entities)
minutes = 0
clock = datetime.now()


while clock.time() < time(15, 30):
    clock = datetime.now()
    if clock.time() > time(9, 14):
        minutes += 1
        while datetime.now().second != 59:  # start at end of minute
            continue

        for entity in entities:
            entity.update_values()
            #similar_lines = list(map(lambda x: x[1], closest_lines(entity.line, minutes)))
            #similar_lines.append(entity.line)
            # print('here')
            plot(entity.line, entity.id)

    else:
        print("waiting " + str(clock.time()))
    sleep(60)
log_data(entities)
