import csv
f = open('output2.csv', 'r')

temperature = 0.0
#f.next()
#for row in csv.reader(f):
#	if float(row[6]) > temperature:
#		temperature = float(row[6])
#		print row[2] + ':' + str(temperature)

sensor = []
for row in csv.reader(f):
	if float(row[6]) >= 40.0:
		if row[2] not in sensor:
			sensor.append(row[2])
			print row[2]

print "The number of sensors is " + str(len(sensor))