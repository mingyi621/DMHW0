import csv
f = open('output2.csv','r')
w = open('output3.csv','w')

sensor = []
unsensor = []

print "Starting deleting the sensors which have temperature not less than 40.0"

for row in csv.reader(f):
	if float(row[6]) >= 40.0:
		if row[2] not in unsensor:
			unsensor.append(row[2])
		if row[2] in sensor:
			sensor.remove(row[2])
			print "The sensor " + row[2] + " has been removed."
	else:
		if row[2] not in sensor and row[2] not in unsensor:
			sensor.append(row[2])

print str(len(unsensor)) + " sensors have been removed."
print "Starting to remove data due to PM2.5 and humidity."

g = open('output2.csv','r')

for row in csv.reader(g):
	if row[2] in sensor:
		if float(row[7]) <= 100.0 and float(row[7]) >= 0.0 and float(row[3]) > 0.0 and float(row[3]) <= 100:
			csv.writer(w).writerow(row)

print "The result has been outputed to output3.csv"