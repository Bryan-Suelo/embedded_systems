import csv
import os
import statistics

import numpy as np

#directory = 'results'
directory = 'one_minute_interval'
rssi = []
files = []

for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f):
		files.append(f)
		with open(f, newline='') as infh:
			reader = csv.reader(infh)
			for row in reader:
				if row[2] != 'rssi':
					rssi.append(int(row[2]))


print('Total files in folder: ', len(rssi))
print('Average calculated: ', round(statistics.mean(rssi),2))
print('Min value: ', min(rssi))
print('Max value: ', max(rssi))
print('Standard deviation: ', round(statistics.pstdev(rssi),2))
