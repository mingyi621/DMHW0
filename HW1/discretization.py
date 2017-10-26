import csv
#import sys
f = open('input.csv','r')
w = open('output1.csv','w')

# discretization parameters
n1 = 10 # for PM2.5
n2 = 10 # for PM10
n3 = 10 # for PM1
n4_start = 2.0 # start of temperature
n4 = 4.0 # for temperature
n5 = 10 # for humidity
count = 0

next(csv.reader(f))
for row in csv.reader(f):
	# discretize PM2.5
	if row[3] != 'nan':
		row[3] = float(row[3])
		row[3] = row[3] - row[3] % n1
		row[3] = str(row[3])

	# discretize PM10
	if row[4] != 'nan':
		row[4] = float(row[4])
		row[4] = row[4] - row[4] % n2
		row[4] = str(row[4])

	# discretize PM1
	if row[5] != 'nan':
		row[5] = float(row[5])
		row[5] = row[5] - row[5] % n3
		row[5] = str(row[5])

	# discreteize temperature
	if row[6] != 'nan':
		row[6] = float(row[6])
		row[6] = row[6] - n4_start
		row[6] = row[6] - row[6] % n4
		row[6] = row[6] + n4_start
		row[6] = str(row[6])

	# discrete humidity
	if row[7] != 'nan':
		row[7] = float(row[7])
		row[7] = row[7] - row[7] % n5
		row[7] = str(row[7])

	csv.writer(w).writerow(row)
	count = count + 1
#	sys.stdout.write("\r%d" % count)
#	sys.stdout.flush()
#print ''


