# Sort the data by sensors
import csv
import operator

f = open('201703_Taiwan.csv', 'r')
header = next(csv.reader(f))

header = ['Date', 'Time', 'device_id', 'PM2.5', 'PM10', 'PM1', 'Temperature', 'Humidity', 'latitude', 'longitude']

y = open('output.csv','r')
reader = csv.reader(y)
sortedlist = sorted(reader, key=operator.itemgetter(2), reverse = False)

print "sorted"

z = open('output2.csv', 'w')

#csv.writer(z).writerow(header)
for row in sortedlist:
	csv.writer(z).writerow(row)