import EntityClass
from scipy import spatial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
lines = []
def get_lines(minutes):
    global lines
    if len(lines) == 0:
        file_name = EntityClass.past_trades_file_name
        past_trades = pd.read_hdf(file_name, key='PastTrades')
        #print(past_trades)
        for heading in list(past_trades):
            lines.append(past_trades[heading].values)

    return [x[:minutes] for x in lines]


def closest_lines(core_line, minutes):

    lines = get_lines(minutes)
    #print(lines)
    core_line = np.array(core_line)
    similarities = map(lambda x: spatial.distance.euclidean(core_line, x), lines)
    similarities = sorted(zip(similarities, lines), key=lambda x: x[0])[:3]
    print(similarities)
    return similarities


if __name__ == '__main__':
    minutes = 10
    reference_line = get_lines(minutes)[0]  # arbit constant
    #print(reference_line)
    lines = closest_lines(reference_line, minutes)
    for i in range(0, 2):
        plt.plot(lines[i][1])
    plt.xticks(list(range(0, 60)))
    plt.show()
