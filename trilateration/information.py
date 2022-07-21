import csv
import os
import statistics

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


Dict = {'Beacon3':[], 'Beacon4':[], 'Beacon5':[], 'Beacon6':[], 'Beacon7':[],
	'Beaco10':[], 'Beaco11':[], 'Beaco12':[], 'Beaco13':[],  'Beaco17':[],
	'Beaco18':[], 'Beaco19':[], 'Beaco20':[], 'Test1':[]}

#directory = 'results'
#directory = 'five_minutes_interval'
#directory = 'one_minute_interval'
#directory = 'thirty_seconds_interval'
#directory = 'fifteen_seconds_interval'
directory = 'ten_seconds_reference'

#rssi = np.array([])
files = []

for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f):
		files.append(f)
		with open(f, newline='') as infh:
			reader = csv.reader(infh)
			for row in reader:
				for key in Dict.keys():
					if row[0] == key:
						Dict[key].append(int(row[2]))

print('Data from each device\n')

for key, value in Dict.items():
	print(key)
	print('Total files in folder: ', len(value))
	print('Average calculated: ', round(statistics.mean(value),2))
	print('Min value: ', min(value))
	print('Max value: ', max(value))
	print('Standard deviation: ', round(statistics.pstdev(value),2))
	print('\n')


#for key, value in Dict.items():
#	plt.hist(value)
#	plt.show()
