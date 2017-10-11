import csv
f = open('output2.csv','r')

sensor = []

count = 0

for row in csv.reader(f):
	if sensor != [] and row[2] != sensor:
		if count == 1:
			print sensor
		count = 0
		sensor = row[2]
	else:
		sensor = row[2]
		count = count + 1
