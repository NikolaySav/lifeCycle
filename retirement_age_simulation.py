from statistics import mean, stdev, variance, median

import seaborn as sns
from matplotlib import pyplot
from scipy.stats.mstats import mode

from Classes.Portfolio import *
from Classes.Year import Year
from helpers import *

iterations = 1000000


def simulate(start_stocks=StartingPortfolio.stocks, lc=True) -> int:
    target_wealth = 12000000
    current_wealth = 71873.20
    lc_portfolio = Portfolio(start_stocks, lc)
    annuity = 71873.20

    age = Investor.start_age

    while current_wealth < target_wealth:
        lc_portfolio.adjust_portfolio(age)

        rm = calc_rm(Year.rm_mean, Year.rm_deviation)
        rf = calc_rm(Year.rf_mean, Year.rf_deviation)

        stocks_value = current_wealth * lc_portfolio.stocks * (1 + rm)
        fixed_value = current_wealth * lc_portfolio.fixed * (1 + rf)

        current_wealth = stocks_value + fixed_value + annuity

        age += 1

    return age


def show_dist(start_stocks=StartingPortfolio.stocks, lc=True):
    ages = []
    for iteration in range(0, iterations):
        ages.append(simulate(start_stocks, lc))

    min_age = min(ages)
    max_age = max(ages)
    for pa in range(60, 66):
        print('probability for age ', pa, ': ', calc_probability(ages, pa))
    print('mean: ', mean(ages))
    print('stdev: ', stdev(ages))
    print('variance: ', variance(ages))
    print('mode: ', mode(ages))
    print('median: ', median(ages))
    print('min age: ', min_age)
    print('max age: ', max_age)
    print('interval (max-min): ', max_age - min_age)

    sns.distplot(ages, norm_hist=True, kde=False, bins=np.arange(min_age, max_age + 1))

    # with open('ages100.txt', mode='wt', encoding='utf-8') as file:
    #     file.write('\n'.join((str(i) for i in set(ages))))
    # sns.kdeplot(ages, shade=True)

    # pyplot.hist(ages, density=True)

    pyplot.show()


# вероятность выхода на пенсию раньше или в возрасте age
def calc_probability(ages: list, age: int) -> float:
    length = len(ages)
    counter = 0
    for a in ages:
        if a <= age:
            counter += 1
    return counter / length


if __name__ == "__main__":
    # для портфеля ЖЦ
    print('Life Cycle: ')
    show_dist()
    # print('=================================')
    # для классического
    # print('Classic NPF')
    # show_dist(EndingPortfolio.stocks, False)
