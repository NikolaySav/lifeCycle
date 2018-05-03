from scipy.stats.mstats import gmean

from helpers import *
from .Portfolio import Portfolio


class Year:
    rm_mean = 0.1017
    rf_mean = 0.063

    rm_deviation = 0.2182
    rf_deviation = 0.0578

    def __init__(self,
                 lc_portfolio: Portfolio,
                 classic_portfolio: Portfolio,
                 ):
        self.rf = self._calc_rf()
        self.rm = self._calc_rm()

        self.lc_portfolio = lc_portfolio
        self.classic_portfolio = classic_portfolio

        self.lc_multiplier = self._calc_lc_multiplier()
        self.classic_multiplier = self._calc_classic_multiplier()

        self.lc_g_mean = None
        self.classic_g_mean = None

    def _calc_rm(self):
        return calc_rm(self.rm_mean, self.rm_deviation)

    def _calc_rf(self):
        return calc_rm(self.rf_mean, self.rm_deviation)

    def _calc_lc_multiplier(self):
        return 1 + (self.lc_portfolio.stocks * self.rm + self.lc_portfolio.fixed * self.rf)

    def _calc_classic_multiplier(self):
        return 1 + (self.classic_portfolio.stocks * self.rm + self.classic_portfolio.fixed * self.rf)

    def set_lc_g_mean(self, lc_g_mean_list: list):
        self.lc_g_mean = gmean(lc_g_mean_list) if lc_g_mean_list else self.lc_multiplier

    def set_classic_g_mean(self, classic_g_mean_list: list):
        self.classic_g_mean = gmean(classic_g_mean_list) if classic_g_mean_list else self.classic_multiplier
