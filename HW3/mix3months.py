# mix three month to one file.
import csv
f = open('201701_Taiwan.csv','r')
g = open('201702_Taiwan.csv','r')
h = open('201703_Taiwan.csv','r')
out = open('201701to03_Taiwan.csv','w')

next(csv.reader(f))
next(csv.reader(g))
next(csv.reader(h))

day = ''

for row in csv.reader(f):
	csv.writer(out).writerow(row)
	if day != row[0]:
		print row[0]
	day = row[0]

for row in csv.reader(g):
	csv.writer(out).writerow(row)
	if day != row[0]:
		print row[0]
	day = row[0]

for row in csv.reader(h):
	csv.writer(out).writerow(row)
	if day != row[0]:
		print row[0]
	day = row[0]
