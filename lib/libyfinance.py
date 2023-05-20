#
# Copyright (c) 2023 Gabriel Correa <gabriel.correasb@protonmail.com>
#

import yfinance as yf
import pandas as pd

class Ticker():
	def __init__(self, ticker, period, interval):
		self._ticker = ticker
		self._period = period
		self._interval = interval

	def gen_ticks(self):
		ticker_data = yf.download(tickers=self._ticker, period=self._period, interval=self._interval)
		ticker_data.to_csv('../etc/ticker_data.csv')
