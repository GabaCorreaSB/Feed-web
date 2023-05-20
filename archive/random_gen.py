import random
import time
from datetime import datetime as dt

print('Time,Bid,Ask,Diff')
old = 0
old2 = 0
while True:
	int_number = 5
	float_number = round(int_number+random.random(), 3)

	int_number2 = 5
	float_number2 = round(int_number2+random.random(),3)

	#if not old and not old2:
	#	old = float_number
	#	old2 = float_number2
	#	continue

	#if old < float_number:
	#	old = 0

	#if old2 < float_number2:
	#	old2 = 0
	
	date_now = dt.now().strftime('%H:%M:%S.%f')[:-4]
	#if old > float_number and old2 > float_number2:
	diff = abs(round(float_number - float_number2, 3))
	print(f'{date_now},{float_number},{float_number2},{diff}')
	time.sleep(1)
