import csv
import sys
from geopy.distance import vincenty

f = open('output1.csv','r')
w = open('output3.csv','w')

sensors = []
lat = []
lon = []
dist = []

dist_discretize = 10

# Add sensors and lat, lon informations
for row in csv.reader(f):
	if row[2] not in sensors:
		sensors.append(row[2])
		lat.append(row[8])
		lon.append(row[9])
		sys.stdout.write("\r%d sensors have been appended." % len(sensors))
		sys.stdout.flush()
print ''

sensor = '74DA3895E1AC'

for s,la,lo in zip(sensors, lat, lon):
	if s == sensor:
		base = (float(la),float(lo))
		break

for s,la,lo in zip(sensors, lat, lon):
	place = (float(la),float(lo))
	dist.append(vincenty(base, place).kilometers)

# discretize distance
discretized_dist = []
for d in dist:
	if d % dist_discretize != 0:
		d = d - d % dist_discretize + dist_discretize
	else:
		d = d
	discretized_dist.append(int(d))

# write transactions
date = '2017-03-27'
#time = '12:00:00'
transaction = [0,0]

dictionary = dict(zip(sensors,discretized_dist))

f.seek(0)
# load the PM2.5 for sensor
sensorPM2_5 = []
for row in csv.reader(f):
	if row[2] == sensor:
		sensorPM2_5.append(row[3])

f.seek(0)
count = 0
for row in csv.reader(f):
	if row[3] != 'nan' and sensorPM2_5[count] != 'nan':
		transaction[0] = 'diff = ' + str(abs(float(sensorPM2_5[count])-float(row[3])))
	count = count + 1
	if count == len(sensorPM2_5):
		count = 0	
	transaction[1] = 'distance = ' + str(dictionary[row[2]])
	if row[0] == date and row[3] != 'nan':
		csv.writer(w).writerow(transaction)


