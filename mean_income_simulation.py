import operator
from datetime import datetime
from statistics import mean, stdev, variance, median

from scipy.stats.mstats import mode

from Classes.Investor import Investor
from Classes.Portfolio import Portfolio, StartingPortfolio
from Classes.Year import Year
from helpers import find_negative_count
from progress import update_progress

start_time = datetime.now()

iterations = 100
simulations = []

total_lc_g_means = []
total_classic_g_means = []

for iteration in range(0, iterations):
    simulation = []

    lc_multipliers = []
    lc_g_means = []

    classic_multipliers = []
    classic_g_means = []

    age = Investor.start_age
    while age <= Investor.end_age:
        LCPortfolio = Portfolio(StartingPortfolio.stocks, True)
        LCPortfolio.adjust_portfolio(age)

        ClassicPortfolio = Portfolio(0.1)

        y = Year(LCPortfolio, ClassicPortfolio)

        lc_multipliers.append(y.lc_multiplier)
        classic_multipliers.append(y.classic_multiplier)

        y.set_lc_g_mean(lc_multipliers)
        y.set_classic_g_mean(classic_multipliers)

        lc_g_means.append(y.lc_g_mean)
        classic_g_means.append(y.classic_g_mean)

        age += 1

    total_lc_g_means += lc_g_means
    total_classic_g_means += classic_g_means

    update_progress('Running simulations', iteration / iterations)


update_progress('Simulations complete', 1)

mean_diffs = list(map(operator.sub, total_lc_g_means, total_classic_g_means))
negatives = find_negative_count(mean_diffs)
negative_probability = negatives / len(mean_diffs)

min_diff = min(mean_diffs)
max_diff = max(mean_diffs)

print('mean: ', mean(mean_diffs))
print('stdev: ', stdev(mean_diffs))
print('variance : ', variance(mean_diffs))
print('median: ', median(mean_diffs))
print('mode: ', mode(mean_diffs))
print('min: ', min_diff)
print('max: ', max_diff)
print('interval: ', max_diff - min_diff)

print('print: a=', Portfolio.a)
print('print: b=', Portfolio.b)
print('iterations: ', iterations)
print('Time spent: ', (datetime.now() - start_time))
print('negative probability: ', round(negative_probability, 4))
print('positive probability: ', round((1 - negative_probability), 4))
