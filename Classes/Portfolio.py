import numpy as np

from .Investor import Investor


class StartingPortfolio:
    stocks = 0.9
    fixed = 0.1


class EndingPortfolio:
    stocks = 0.1
    fixed = 0.9


class Portfolio:

    @staticmethod
    def get_coefficients():
        # a - b*f = r
        # a - b * 30 = 0.8
        # a - b * 60 = 0.2
        # a = np.array([[1, 30], [1, 50]])
        a = np.array([[1, Investor.declining_start_age], [1, Investor.declining_stop_age]])
        b = np.array([StartingPortfolio.stocks, EndingPortfolio.stocks])
        return np.linalg.solve(a, b)

    # noinspection PyUnresolvedReferences
    [a, b] = get_coefficients.__func__()

    def __init__(self, stocks, lc=False):
        self.stocks = stocks
        self.fixed = 1 - self.stocks
        self.lc = lc

    def adjust_portfolio(self, age: int):
        if self.lc:
            if age <= Investor.declining_start_age:
                self.stocks = StartingPortfolio.stocks
                self.fixed = StartingPortfolio.fixed
            elif age >= Investor.declining_stop_age:
                self.stocks = EndingPortfolio.stocks
                self.fixed = EndingPortfolio.fixed
            else:
                self.stocks = Portfolio.a + Portfolio.b * age
                self.fixed = 1 - self.stocks


if __name__ == '__main__':
    # from .Investor import Investor
    # print(Portfolio.a)
    # print(Portfolio.b)
    # a = np.array([[1, 30], [1, 50]])
    # b = np.array([StartingPortfolio.stocks, EndingPortfolio.stocks])
    # np.linalg.solve(a, b)
    print(Portfolio.get_coefficients())
