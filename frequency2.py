import csv
f = open('frequency.csv','r')
w = open('frequency2.csv','w')

indicator = 1
index = 1

for row in csv.reader(f):
	if index < len(row):
		if int(row[index]) <= 24:
			continue
		else:
			index = index + 1
		csv.writer(w).writerow(row)
	index = 1






#	index = 0
#	for element in row:
#		if index == 0:
#			index = index + 1
#			continue
#		if int(element) < 10:
#			print element
#			indicator = 0
#			break
#		index = index + 1
#	if indicator == 1:
#		csv.writer(w).writerow(row)
#		print row

