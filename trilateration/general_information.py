import csv
import os
import statistics

#import pandas as pd
#import numpy

directory = 'results'
rssi = []
files = []

for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f):
		files.append(f)
		with open(f, newline='') as infh:
			reader = csv.reader(infh)
			for row in reader:
				if row[0] == 'MBeacon':
					rssi.append(int(row[2]))

#print(len(files))
print('Total files in folder: ', len(rssi))
print('Average calculated: ', round(statistics.mean(rssi),2))
print('Min value: ', min(rssi))
print('Max value: ', max(rssi))
print('Standard deviation: ', round(statistics.pstdev(rssi),2))
