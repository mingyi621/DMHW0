import csv
import random

def checkGoodSensor(data):
	result = ['0','']
	if len(data) < 1*24*90:
		result = ['0', 'Length of data is too short.']
	elif data[0][4] == '0':
		result = ['0', 'PM10 is 0']
	elif data[0][0] != '2017-01-01' or data[len(data)-1][0] != '2017-03-31':
		result = ['0', 'Data is incomplete.']
	else:
		result = ['1', '']
	return result

f = open('201701to03_Taiwan.csv','r')
g = open('oneSensorOrigin.csv','w')

sensors = []

for row in csv.reader(f):
	if row[2] not in sensors:
		sensors.append(row[2])
		print row[2] + ' ' + str(len(sensors))

numOfSensors = len(sensors)
print numOfSensors

while True:
	randomSensor = random.randint(0,numOfSensors-1)
	print 'randomSensor is number ' + str(randomSensor) +' = '+ sensors[randomSensor] 

	f.seek(0)
	data = []

	for row in csv.reader(f):
		if row[2] == sensors[randomSensor]:
			data.append(row)

	result = checkGoodSensor(data)

	if result[0] == '0':
		print result[1]
		print sensors[randomSensor] + ' is not a good sensor.'
	else:
		print 'length of data is ' + str(len(data))
		print sensors[randomSensor] + ' is a good sensor.'
		break

for element in data:
	csv.writer(g).writerow(element)






