## Lib to generate the charts properties
##
## Copyright (c) 2023 Gabriel Correa <gabriel.correasb@protonmail.com>
##

def bidask_line_graph():
	properties = {
		"mode":"lines",
		"x": "Datetime",
		"y[1]":"High",
		"y[2]":"Low",
		"y[3]":"Close",
		"color[1]":"blue",
		"color[2]":"red",
		"color[3]":"yellow"	
		}

	return properties

def bidask_bar_graph():
	properties = {
		"type":"bar",
		"x":"Datetime",
		"y[1]":"High",
		"y[2]":"Low",
		"y[3]":"Close",
		"color[1]":"blue",
		"color[2]":"red",
		"color[3]":"yellow"
		}

	return properties

def ticker_candle_graph():
	properties = {
		"type":"candlestick",
		"x":"Datetime",
		"open":"Open",
		"close":"Close",
		"low":"Low",
		"high":"High"
		}

	return properties
