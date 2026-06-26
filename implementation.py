import numpy as np
import torch

class PathwiseFinance:
    def __init__(self, initial_price, time_steps, dt):
        self.initial_price = initial_price
        self.time_steps = time_steps
        self.dt = dt

    def generate_price_path(self, drift, volatility, seed=None):
        if seed is not None:
            torch.manual_seed(seed)
        increments = torch.randn(self.time_steps) * np.sqrt(self.dt)
        path = torch.zeros(self.time_steps + 1)
        path[0] = self.initial_price
        for t in range(1, self.time_steps + 1):
            path[t] = path[t - 1] * (1 + drift * self.dt + volatility * increments[t - 1])
        return path

    def asian_option_payoff(self, price_path, strike_price):
        average_price = torch.mean(price_path)
        return torch.maximum(average_price - strike_price, torch.tensor(0.0))

    def hedge_portfolio(self, price_path, strike_price):
        portfolio_value = torch.zeros(self.time_steps + 1)
        delta = torch.zeros(self.time_steps)
        portfolio_value[0] = self.asian_option_payoff(price_path, strike_price)

        for t in range(self.time_steps):
            delta[t] = (portfolio_value[t] - self.asian_option_payoff(price_path[t:], strike_price)) / price_path[t]
            portfolio_value[t + 1] = portfolio_value[t] + delta[t] * (price_path[t + 1] - price_path[t])

        return portfolio_value, delta

if __name__ == '__main__':
    initial_price = 100.0
    time_steps = 50
    dt = 1 / 252  # Daily steps in a year
    drift = 0.05
    volatility = 0.2
    strike_price = 105.0

    model = PathwiseFinance(initial_price, time_steps, dt)
    price_path = model.generate_price_path(drift, volatility, seed=42)
    portfolio_value, delta = model.hedge_portfolio(price_path, strike_price)

    print("Generated Price Path:", price_path)
    print("Portfolio Value:", portfolio_value)
    print("Delta (Hedging Strategy):", delta)