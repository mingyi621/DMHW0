import csv
import matplotlib.pyplot as plt

f = open('input.csv','r')

sensor = '74DA3895DF4C'
date = '2017-03-23'

PM2_5 = []
temperature = []
humidity = []

next(csv.reader(f))

for row in csv.reader(f):
	if row[2] == sensor and row[0] == date:
		if row[3] == 'nan':
			row[3] = 0
		if row[6] == 'nan':
			row[6] = 0
		if row[7] == 'nan':
			row[7] = 0
		PM2_5.append(row[3])
		temperature.append(row[6])
		humidity.append(row[7])

plt.plot(PM2_5)
plt.show()
plt.plot(temperature)
plt.show()
plt.plot(humidity)
plt.show()

