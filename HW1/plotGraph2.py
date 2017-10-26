import csv
import matplotlib.pyplot as plt

f = open('output1.csv','r')
next(csv.reader(f))

sensor1 = '74DA3895E1AC'
sensor2 = '74DA3895E018'
date = '2017-03-27'

pm2_5_1 = []
pm10_1 = []
pm1_1 = []
x_1 = []
count = 0

for row in csv.reader(f):
	if row[2] == sensor1 and row[0] == date:
		pm2_5_1.append(row[3])
		pm10_1.append(row[4])
		pm1_1.append(row[5])
		count = count + 1
		x_1.append(count)

#plt.plot(x_1,pm2_5_1)
#plt.plot(x_1,pm10_1)
#plt.plot(x_1,pm1_1)

f.seek(0)
next(csv.reader(f))

pm2_5_2 = []
pm10_2 = []
pm1_2 = []
x_2 = []
count = 0

for row in csv.reader(f):
	if row[2] == sensor2 and row[0] == date:
		pm2_5_2.append(row[3])
		pm10_2.append(row[4])
		pm1_2.append(row[5])
		count = count + 1
		x_2.append(count)

plt.plot(x_2,pm2_5_2)
plt.plot(x_2,pm10_2)
plt.plot(x_2,pm1_2)



plt.show()


