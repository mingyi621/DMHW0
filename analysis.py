import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from geopy.distance import vincenty

def reverseTimestamp(stamp):
	second = stamp % 60
	stamp = stamp - second
	minute = (stamp % 3600) / 60
	stamp = stamp - minute * 60
	hour = (stamp % 86400) / 3600
	stamp = stamp - hour * 3600
	day = stamp / 86400

	date = '2017-03-' + str(day).zfill(2)
	time = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

	return date, time

def offsetTranslation(data):
	a = np.array(data)
	mean = np.mean(a)

	for element in data:
		element = element - mean

	return data

def amplitudeScaling(data):
	a = np.array(data)
	mean = np.mean(a)
	std = np.std(a)

	for e in data:
		e = (e-mean)/std

	return data

r = open('output5.csv', 'r')

catagory = next(csv.reader(r))
sensors = []
lat = []
lon = []

for row in csv.reader(r):
	if row[2] not in sensors:
		sensors.append(row[2])
		lat.append(row[8])
		lon.append(row[9])
		sys.stdout.write("\r%d sensors have been appended." % len(sensors))
		sys.stdout.flush()
print ''

print sensors

time = []
num = 0

while num < 86400:
	time.append(num)
	num = num + 900

date = '2017-03-' + raw_input("date = ")
sensor1 = raw_input("sensor = ")

r.seek(0)
next(csv.reader(r))

pm2_5_1 = []
location = [0.0,0.0]

for row in csv.reader(r):
	if row[2] == sensor1 and date == row[0]:
		if row[3] == 'nan':
			pm2_5_1.append(float('0'))
		else:
			pm2_5_1.append(float(row[3]))
	if row[2] == sensor1:
		location[0] = row[8]
		location[1] = row[9]

plt.plot(time,pm2_5_1)

nearest = []

for s,la,lo in zip(sensors, lat, lon):
	place1 = (float(location[0]),float(location[1]))
	place2 = (float(la),float(lo))
	distance1_2 = vincenty(place1, place2).kilometers
	if distance1_2 <= 5.0 and distance1_2 > 0:
		nearest.append((s,round(distance1_2,2)))

for i in nearest:
	print i

sensor2 = raw_input("sensor = ")

r.seek(0)
next(csv.reader(r))
pm2_5_2 = []

for row in csv.reader(r):
	if row[2] == sensor2 and date == row[0]:
		if row[3] == 'nan':
			pm2_5_2.append(float('0'))
		else:
			pm2_5_2.append(float(row[3]))

plt.plot(time,pm2_5_2)

plt.show()