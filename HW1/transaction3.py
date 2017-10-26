import csv
import numpy as np
import sys
from geopy.distance import vincenty
import matplotlib.pyplot as plt

def euclideanDistance(data1,data2):
	a = np.array(data1)
	b = np.array(data2)
	dist = np.linalg.norm(a - b)
	return dist

def offsetTranslation(data):
	a = np.array(data)
	mean = np.mean(a)

	data2 = []
	e2 = 0

	for element in data:
		e2 = element - mean
		data2.append(e2)

	return data2

f = open('input.csv','r')
w = open('output4.csv','w')

sensors = []
lat = []
lon = []
dist = []

dist_discretize = 100
eu_dist_discretize = 600
eu_base = 300

next(csv.reader(f))
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

f.seek(0)
next(csv.reader(f))
data1 = []

for row in csv.reader(f):
	if row[2] == sensor:
		if row[3] == 'nan':
			row[3] = 0
		data1.append(float(row[3]))

#data1 = offsetTranslation(data1)

eu_dist = []
data2 = []
f.seek(0)
next(csv.reader(f))
last_sensor = ''
e = 0

for row in csv.reader(f):
	if last_sensor != '' and row[2] != last_sensor:
#		data2 = offsetTranslation(data2)
		eu_dist.append(euclideanDistance(data1,data2))
		data2 = []
	if row[3] == 'nan':
		row[3] = 0
	last_sensor = row[2]
	data2.append(float(row[3]))

eu_dist.append(euclideanDistance(data1,data2))

discreted_eu_dist = []
for eu in eu_dist:
	if (eu - eu_base) % eu_dist_discretize != 0:
		discreted_eu_dist.append( (eu-eu_base) + eu_dist_discretize - (eu-eu_base) % eu_dist_discretize + eu_base)
	else:
		discreted_eu_dist.append(eu)


transaction = [0,0]

for d,eu_d in zip(discretized_dist,discreted_eu_dist):
	transaction[0] = 'dist = ' + str(d)
	transaction[1] = 'eu_dist = ' + str(eu_d)
	csv.writer(w).writerow(transaction)

#print eu_dist

#plt.plot(eu_dist)


#plt.plot(dist)


#plt.show()








