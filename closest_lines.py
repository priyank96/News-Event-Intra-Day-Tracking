import EntityClass
from scipy import spatial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import timedelta, date, datetime
from dateutil.parser import parse

lines_hl = []
lines_date = []


def get_lines_hl(minutes):
    global lines_hl
    if len(lines_hl) == 0:
        file_name = EntityClass.past_trades_file_name
        past_trades = pd.read_hdf(file_name, key='headline')
        for heading in list(past_trades):
            lines_hl.append(past_trades[heading].values)

    return [x[:minutes] for x in lines_hl]


def get_lines_date(minutes):

    global lines_date
    if len(lines_date) == 0:
        if datetime.now().isoweekday() == 1:
            yesterday = date.today() - timedelta(3)
        else:
            yesterday = date.today() - timedelta(1)

        file_name = EntityClass.past_trades_file_name
        past_trades = pd.read_hdf(file_name, key='date')
        for heading in past_trades.columns:
            if parse(heading, fuzzy=True) == yesterday:
                lines_date.append(past_trades[heading].values)

    return [x[:minutes] for x in lines_date]


def closest_lines(core_line, minutes):
    lines_hl = get_lines_hl(minutes)
    lines_date = get_lines_date(minutes)
    core_line = np.array(core_line)
    similarities_hl = map(lambda x: spatial.distance.euclidean(core_line, x), lines_hl)
    similarities_date = map(lambda x: spatial.distance.euclidean(core_line, x), lines_date)

    similarities = [sorted(zip(similarities_hl, lines_hl), key=lambda x: x[0])[0],
                    sorted(zip(similarities_date, lines_date), key=lambda x: x[0])[0]]
    # closest line in general and closest most of most recent lines
    return similarities


if __name__ == '__main__':
    minutes = 10
    reference_line = get_lines_hl(minutes)[0]  # arbit constant
    lines = closest_lines(reference_line, minutes)
    for i in range(0, 2):
        plt.plot(lines[i][1])
    plt.xticks(list(range(0, 60)))
    plt.show()
