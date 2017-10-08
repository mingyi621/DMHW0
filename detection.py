import csv
f = open('201703_Taiwan.csv', 'r')

max = 0.0
count = 0

for row in csv.reader(f):
#	if row[2] == "74DA3895C234":
#		print row
	if row[0] == '2017-03-05':
		if row[3] >= max:
			max = row[3]
			print row
			if row[3] == '99':
				count = count + 1
print count
