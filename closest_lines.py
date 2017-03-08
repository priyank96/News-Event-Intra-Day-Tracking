import glob
import csv
from scipy import spatial
import matplotlib.pyplot as plt
import numpy as np


def get_lines():
    minutes = 120
    lines = []
    # lines.append(np.array([0 for x in range(0, minutes)]))
    for name in glob.glob('PastTrades/*'):

        with open(name) as csvfile:
            line = []
            spamreader = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in spamreader:
                count += 1
                if count == 1 and row:
                    start = float(row[1])
                    line.append(0.0)

                elif row:
                    line.append((float(row[1]) - start) * 100 / start)
                if count == 2 * minutes:
                    line = np.array(line)
                    lines.append(line)
                    break

    return lines


def closest_lines(core_line,minutes):
    lines = get_lines()
    #print('closestlines: ', lines)
    # core_line = core_line[:minutes]
    core_line = np.array(core_line)
    similarities = map(lambda x: spatial.distance.sqeuclidean(core_line, x[:minutes]), lines)
    similarities = sorted(zip(similarities, lines), key=lambda x: x[0])[:3]
    return similarities


if __name__ == '__main__':
    reference_line = get_lines()[4]  # arbit constant
    lines = closest_lines(reference_line, 1)
    for i in range(0, 3):
        plt.plot(lines[i][1])
    plt.xticks(list(range(0, 60)))
    plt.show()
