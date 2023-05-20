from taipy import Gui
import pandas as pd
from libproperties import *

def get_data():
	dataset = pd.read_csv("/Users/gaba/codes/projects/taipy_feed/etc/ticker_data.csv")
	return dataset

data = get_data()
properties_lines = bidask_line_graph()
properties_bar = bidask_bar_graph()
properties_candle = ticker_candle_graph()

page = """
# UBER Ticker info

Data Yfinance Line Chart:
<|{data}|chart|properties=properties_lines|>

Data Yfinance Bar Chart:
<|{data}|chart|properties=properties_bar|>

Data Yfinance Candlestick Chart:
<|{data}|chart|properties=properties_candle|>

"""


Gui(page).run(use_reloader=True)
