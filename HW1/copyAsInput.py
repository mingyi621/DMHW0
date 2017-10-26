import csv
f = open('../HW0/output5.csv','r')
g = open('input.csv','w')

for row in csv.reader(f):
	csv.writer(g).writerow(row)