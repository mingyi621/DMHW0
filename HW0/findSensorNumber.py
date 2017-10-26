import csv
with open('output.csv', 'wb') as out:
	reader = csv.reader(open('201703_Taiwan.csv', 'rb'))
	writer = csv.writer(out, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)

	sensor = []
	for row in reader:
		if row[2] not in sensor:
			sensor.append(row[2])

	print len(sensor)