import csv
import matplotlib.pyplot as plt

f = open('input.csv','r')

sensor = '74DA3895E1AC'
count = 0
x = []
y = []

next(csv.reader(f))
for row in csv.reader(f):
	if row[2] == sensor and row[3] != 'nan' and row[1] == '12:00:00' :
		count = count + 1
		x.append(count)
		y.append(row[3])

plt.plot(x,y)

f.seek(0)
next(csv.reader(f))
count = 0
x = []
y = []

for row in csv.reader(f):
	if row[2] == sensor and row[3] != 'nan' and row[1] == '12:00:00' :
		count = count + 1
		x.append(count)
		y.append(row[4])

plt.plot(x,y)


plt.show()




