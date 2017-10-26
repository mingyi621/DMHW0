import csv
f = open('output2.csv','r')

sensor = []

count = 0

for row in csv.reader(f):
	if sensor != [] and row[2] != sensor:
		if count == 1:
			print sensor
		count = 0
	else:
		count = count + 1
	sensor = row[2]
