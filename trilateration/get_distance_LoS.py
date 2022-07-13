import string
import re
import math 
import csv
import os
import time
#from time import time, sleep, strftime
#import schedule


os.system('sudo blescan | grep "ac:23:3f" > scan.txt')

Dict = {'Beacon3': 'ac:23:3f:65:f7:96', 'Beacon4':'ac:23:3f:65:f7:9a', 'Beacon5': 'ac:23:3f:65:f7:a9', 'Beacon6': 'ac:23:3f:65:f7:9c', 
    'Beacon7': 'ac:23:3f:65:f7:9d', 'Beaco10':'ac:23:3f:65:f7:a7', 'Beaco11': 'ac:23:3f:65:f7:a0', 'Beaco12':'ac:23:3f:65:f7:99', 'Beaco13':'ac:23:3f:65:f7:a5', 
    'Beaco18':'ac:23:3f:65:f7:97', 'Beaco19':'ac:23:3f:65:f7:98', 'Beaco20':'ac:23:3f:65:f7:9b', 'Beaco17':'ac:23:3f:65:f7:9f', 'MBeacon':'ac:23:3f:65:f7:2e'}

findings = {}


# Read file after looking for devices
mac_addr = re.compile(r':*(?:[0-9a-fA-F]:?){12}')
rssi_val = re.compile(r'(^|-)([0-9]+)')

with open('scan.txt') as f:
	lines = f.readlines()
	for line in lines:
		m = re.search(mac_addr, line)
		r = re.search(rssi_val, line)
		if m and r:
			findings[m.group()] = int(r.group())

f.close()

keys = []
vals = []
dist = []
reference_value = -48.37

# Calculate distance Line of Sight (LoS)
for key,val in findings.items():
	distance = 10** ((reference_value -(val))/(10 * 2.4))
	keys.append(key)
	vals.append(val)
	dist.append(distance)

time = time.strftime("%Y%m%d-%H%M%S")
#time = strftime("%Y%m%d-%H%M%S")
file = open('test-' + time + '.csv', 'w', newline='')

with file:
	header = ['name', 'mac', 'rssi', 'distance']
	writer = csv.DictWriter(file, fieldnames = header)
	writer.writeheader()
	for i in range(len(keys)):
		#print(results[i])
		for name,mac in Dict.items():
			#print(results[i])
			if mac == keys[i]:
				writer.writerow({'name':name, 'mac':mac, 'rssi':vals[i], 'distance':dist[i]})

#schedule.every(1).minutes.do(func)
