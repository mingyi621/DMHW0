import csv
f = open('201703_Taiwan.csv', 'r')

for row in csv.reader(f):
	if row[2] == "74DA3895C234":
		print row