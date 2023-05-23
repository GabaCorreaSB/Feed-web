from yahooquery import Ticker
from datetime import datetime

class StockDataWriter:
	def __init__(self, security, file_name):
		self.__security = security
		self.__file_name = file_name
		self.__ticker = Ticker(self.__security)

		# Function to get the initial Bid, Ask and LastPrice 
		def get_initial_data(self):
			data = self.__ticker.quotes[self.__security]
			self.initial_timestamp = datetime.fromtimestamp(data["regularMarketTime"]).isoformat()
			self.initial_bid = str(data['bid'])
			self.initial_ask = str(data['ask'])
			self.initial_last_price = str(data['regularMarketPrice'])

		def write_initial_data_to_csv(self):
			with open(self.__file_name, mode='w') as file:
				file.write('Timestamp,Bid,Ask,LastPrice\n')
				file.write('{self.initial_timestamp},{self.initial_bid},{self.initial_ask}, {self.initial_last_price}\n')

		def process_data(self):
			data = self.__ticker.quotes[self.__symbol]
			timestamp = datetime.fromtimestamp(data['regularMarketTime']).isoformat()
			bid = data['bid']
			ask = data['ask']
			last_price = data['regularMarketPrice']

			if bid != self.initial_bid:
				self.initial_bid = bid
			
			with open(self.__file_name, mode='a', buffering=1) as file:
				file.write(f'{timestamp},{bid},{ask},{last_price}\n')
