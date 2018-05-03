import numpy as np


def calc_rm(mean, deviation):
    return np.random.normal(mean, deviation, 1)[0]


def geo_mean_overflow(iterable):
    a = np.log(iterable)
    return np.exp(a.sum() / len(a))


def find_negative_count(values: list) -> int:
    count = 0
    for item in values:
        if item < 0:
            count += 1
    return count

