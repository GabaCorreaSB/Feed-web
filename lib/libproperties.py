## Lib to generate the charts properties
##
## Copyright (c) 2023 Gabriel Correa <gabriel.correasb@protonmail.com>
##

def bidask_line_graph():
	properties = {
		"mode":"lines",
		"x": "Time",
		"y[1]":"Bid",
		"y[2]":"Ask",
		"y[3]":"Diff",
		"color[1]":"blue",
		"color[2]":"red",
		"color[3]":"yellow"	
		}

	return properties

def bidask_bar_graph():
	properties = {
		"type":"bar",
		"x":"Time",
		"y[1]":"Bid",
		"y[2]":"Ask",
		"y[3]":"Diff",
		"color[1]":"blue",
		"color[2]":"red",
		"color[3]":"yellow"
		}

	return properties
