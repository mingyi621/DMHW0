import csv
f = open('output1.csv','r')
w = open('output2.csv','w')

sensor = '74DA3895DF4C'
transaction = [0,0,0]

for row in csv.reader(f):
	if row[2] == sensor and row[3] != 'nan':
		transaction[0] = 'PM2.5 = ' + row[3]
#		transaction[1] = 'PM10 = ' + row[4]
#		transaction[2] = 'PM1 = ' + row[5]
		transaction[1] = 'Temperature = ' + row[6]
		transaction[2] = 'Humidity = ' + row[7]

		csv.writer(w).writerow(transaction)