from taipy import Gui
import pandas as pd
from libproperties import *

def get_data():
	dataset = pd.read_csv("/Users/gaba/codes/projects/taipy_feed/etc/data.csv")
	return dataset

data = get_data()
properties_lines = bidask_line_graph()
properties_bar = bidask_bar_graph()

page = """
# Bid and Ask ticks with difference

Data Real Time Line Chart:

<|{data}|chart|properties=properties_lines|>
<|
|>
Data Real Time Bar Chart:
<|
|>
<|{data}|chart|properties=properties_bar|>
"""


Gui(page).run(use_reloader=True)
