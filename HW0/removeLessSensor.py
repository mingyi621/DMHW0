import csv
f = open('frequency.csv','r')
g = open('output3.csv','r')
w = open('output4.csv','w')

print "Leave good sensors by frequency."

next(csv.reader(f))

sensor = []

for row in csv.reader(f):
	sensor.append(row[0])

print "Good sensors are appended."

for row in csv.reader(g):
	if row[2] in sensor:
		csv.writer(w).writerow(row)
	
print "The data have been outputed to output4.csv"
