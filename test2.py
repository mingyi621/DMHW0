import csv
f = open('output5.csv', 'r')

next(csv.reader(f))
sensor = []
for row in csv.reader(f):
	if float(row[9]) < 120.0 and float(row[9]) > 117.0 and float(row[8]) > 23.0 and float(row[8]) < 25.0:
		if row[2] not in sensor:
			print row
			sensor.append(row[2])