from libyfinance import *

def terminal_label():
	print("=" * 51)
	print("=" * 14 + " TICKER INFO GENERATOR " + "=" * 14)
	print("=" * 18 + " Made by: Gaba " + "=" * 18)
	print("=" * 51)

def get_info():
	ticker = input("Ticker you wanna plot the charts: ")
	period_ok = 0
	while not period_ok:
		print("MAKE SURE YOU READ THE README FILE TO KNOW WHICH VALUES TO PASS FOR PERIOD AND INTERVAL")
		period = int(input("The period you wanna acquire (Min 2): "))
		if period >= 2:
			period_ok = 1
	

	period = input("Months, days or weeks? (Check readme for inputs): ") + str(period)
	
	interval = input("Time interval (Hours or Minutes *Check readme*): ")

	ticker = Ticker(ticker, period, interval)
	ticker.gen_ticks()

def main():
	terminal_label()
	get_info()

if __name__ == '__main__':
	main()
