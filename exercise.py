import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm


def download_data(stocks, start_date, end_date):
    data = {}
    ticker = yf.download(stocks, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)


def calculate_returns(stock_data):
    stock_data['Price'] = np.log(stock_data['Price'] / stock_data['Price'].shift(1))
    return stock_data[1:]


# fat tails mean that extreme events occur more frequently in reality than what a normal distribution would predict
def show(stock_data):
    plt.hist(stock_data, bins=700)
    stock_variance = stock_data.var()
    stock_mean = stock_data.mean()
    sigma = np.sqrt(stock_variance)
    x = np.linspace(stock_mean - 5 * sigma, stock_mean + 5 * sigma, 100)
    plt.plot(x, norm.pdf(x, stock_mean, sigma))
    plt.show()


if __name__ == '__main__':
    stock_data = download_data('IBM', '2010-01-01', '2020-01-01')
    show(calculate_returns(stock_data))
