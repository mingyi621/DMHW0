# find the number of sensors
import csv
import operator
f = open('201703_Taiwan.csv', 'r')
w = open('output.csv', 'w')

sensor = []
header = next(csv.reader(f))

print "Start detecting sensors in Taiwan:"

for row in csv.reader(f):
	if row[2] not in sensor:
		if float(row[8]) >= 21.5 and float(row[8]) <= 26.5 and float(row[9]) >= 118.0 and float(row[9]) <= 122.0:
			sensor.append(row[2])
		else:
			continue

print "The number of sensors is " + str(len(sensor))

x = open('201703_Taiwan.csv', 'r')
next(csv.reader(x))

#csv.writer(w).writerow(header)

for row in csv.reader(x):
	if row[2] in sensor:
		csv.writer(w).writerow(row)

print "The data of the available sensors have been outputed to output.csv"
print "Starting output the location file."

# Output the location file
y = open('201703_Taiwan.csv', 'r')
next(csv.reader(y))

header = ['Date', 'Time', 'device_id', 'PM2.5', 'PM10', 'PM1', 'Temperature', 'Humidity', 'latitude', 'longitude']

location = open('location.csv','w')

csv.writer(location).writerow(header)

for element in sensor:
	for row in csv.reader(y):
		if row[2] == element:
			csv.writer(location).writerow(row)
			break

print "The location file has been outputed."