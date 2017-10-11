import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from geopy.distance import vincenty
import scipy.signal
from scipy.signal import filtfilt, butter

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

	data2 = []
	e2 = 0

	for element in data:
		e2 = element - mean
		data2.append(e2)

	return data2

def amplitudeScaling(data):
	a = np.array(data)
	mean = np.mean(a)
	std = np.std(a)

	data2 = []
	e2 = 0

	for e in data:
		e2 = (e-mean)/std
		data2.append(e2)

	return data2

def euclideanDistance(data1,data2):
	a = np.array(data1)
	b = np.array(data2)
	dist = np.linalg.norm(a - b)
	return dist

def denoise(data):
#	n = 3
#	b = [1.0/n]*n
#	a = 1
#	data2 = lfilter(b,a,data)

	b, a = butter(3, 0.5)
	data2 = filtfilt(b, a, data)


	return data2

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

#pm2_5_1 = offsetTranslation(pm2_5_1)
#pm2_5_1 = amplitudeScaling(pm2_5_1)
#pm2_5_1 = scipy.signal.detrend(pm2_5_1)
#pm2_5_1 = denoise(pm2_5_1)
#plt.plot(time,pm2_5_1)

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

#pm2_5_2 = offsetTranslation(pm2_5_2)
#pm2_5_2 = amplitudeScaling(pm2_5_2)
#pm2_5_2 = scipy.signal.detrend(pm2_5_2)
#pm2_5_2 = denoise(pm2_5_2)
#plt.plot(time,pm2_5_2)

# The output steps:

# origin figure:
plt.plot(time,pm2_5_1)
plt.plot(time,pm2_5_2)
print "Origin figure:"
print "Eu distance = " + str(euclideanDistance(pm2_5_1,pm2_5_2))
plt.show()
plt.gcf().clear()

# 1st step: offset translation
pm2_5_1 = offsetTranslation(pm2_5_1)
pm2_5_2 = offsetTranslation(pm2_5_2)
plt.plot(time,pm2_5_1)
plt.plot(time,pm2_5_2)
print "After offset translation:"
print "Eu distance = " + str(euclideanDistance(pm2_5_1,pm2_5_2))
plt.show()
plt.gcf().clear()

# 2nd step: amplitude scaling
pm2_5_1 = amplitudeScaling(pm2_5_1)
pm2_5_2 = amplitudeScaling(pm2_5_2)
plt.plot(time,pm2_5_1)
plt.plot(time,pm2_5_2)
print "After amplitude scaling:"
print "Eu distance = " + str(euclideanDistance(pm2_5_1,pm2_5_2))
plt.show()
plt.gcf().clear()

# 3rd step: detrend
pm2_5_1 = scipy.signal.detrend(pm2_5_1)
pm2_5_2 = scipy.signal.detrend(pm2_5_2)
plt.plot(time,pm2_5_1)
plt.plot(time,pm2_5_2)
print "After detrend:"
print "Eu distance = " + str(euclideanDistance(pm2_5_1,pm2_5_2))
plt.show()
plt.gcf().clear()

# 4th step: denoise
pm2_5_1 = denoise(pm2_5_1)
pm2_5_2 = denoise(pm2_5_2)
plt.plot(time,pm2_5_1)
plt.plot(time,pm2_5_2)
print "After denoise:"
print "Eu distance = " + str(euclideanDistance(pm2_5_1,pm2_5_2))
plt.show()
plt.gcf().clear()




