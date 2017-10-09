import csv
f = open('output3.csv','r')
w = open('frequency.csv','w')

print "Starting detecting the frequency."

sensor = []
count = 0
r = []
ind = 0
min = 1000

empty = ['']
number = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
header = empty + number
csv.writer(w).writerow(header)

for row in csv.reader(f):
	if row[2] != sensor:
		if r != []:
			r.append(str(count))
			if count < min:
				min = count
			if min >=24 and len(r) == 32:
				csv.writer(w).writerow(r)
			min = 1000
			r = []
		r.append(row[2])
		sensor = row[2]
		count = 0
		ind = 0
	while ind < 31:
		if row[0] == '2017-03-' + number[ind]:
			count = count + 1
			break
		else:
			r.append(str(count))
			if count < min:
				min = count
			ind = ind + 1
			count = 0

print "The last append:"
r.append(str(count))
if count < min:
	min = count
if min >=24 and len(r) == 32:
	csv.writer(w).writerow(r)

print "The frequency file has been outputed to frenquency.csv"