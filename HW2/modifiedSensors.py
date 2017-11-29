import csv
f = open('input.csv','r')
w = open('location_modified.csv','w')
next(csv.reader(f))

sensors = []
for row in csv.reader(f):
	if row[2] not in sensors:
		sensors.append(row[2])
		csv.writer(w).writerow(row)


