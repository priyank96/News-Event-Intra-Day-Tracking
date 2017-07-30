import EntityClass
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

dict_of_past_trades = dict()


def format_lines(data):
    if len(dict_of_past_trades) == 0:
        for key in data:
            if np.isnan(data[key]).any():
                # slicing arrays to remove NaNs
                for key in data.keys():
                    if np.isnan(data[key]).any():
                        first_nan_occurrence = np.where(np.isnan(data[key]))[0][0]
                        dict_of_past_trades[key] = list(data[key])[0:first_nan_occurrence]

                    else:
                        dict_of_past_trades[key] = list(data[key])
                        # print(dict_of_past_trades[key])


def get_closest_line(line):
    similarity_scores = []
    for key in dict_of_past_trades.keys():
        distance, path = fastdtw(line, dict_of_past_trades[key], dist=euclidean)
        similarity_scores.append((dict_of_past_trades[key], distance))

    return list(map(lambda x: x[0], sorted(similarity_scores, key=lambda x: x[1])[0:2]))
