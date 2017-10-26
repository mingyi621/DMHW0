import csv
f = open('input.csv','r')
w = open('output5.csv','w')

discretize_PM2_5 = 10
discretize_temperature = 1
discretize_humidity = 5
time_interval = 1 # hour

next(csv.reader(f))
count_hour = 0
last = []
transaction = [0,0,0]
sensor = ''

for row in csv.reader(f):
	if row[1] == str(count_hour).zfill(2) + ':00:00':
		if sensor != '' and row[2] != sensor:
			last = []
			sensor = row[2]
			count_hour = 0
		count_hour = count_hour + time_interval
		if count_hour >= 24:
			count_hour = count_hour - 24
		sensor = row[2]
		if last == []:
			last = row
			continue

		incre_PM2_5 = float(row[3]) - float(last[3])
		incre_temperature = float(row[6]) - float(last[6])
		incre_humidity = float(row[7]) - float(last[7])

		incre_PM2_5 = round(incre_PM2_5 / discretize_PM2_5) * discretize_PM2_5
		incre_temperature = round(incre_temperature / discretize_temperature) * discretize_temperature
		incre_humidity = round(incre_humidity / discretize_humidity) * discretize_humidity

		transaction[0] = 'increment of PM2.5 = ' + str(incre_PM2_5)
		transaction[1] = 'increment of temperature = ' + str(incre_temperature)
		transaction[2] = 'increment of humidity = ' + str(incre_humidity)
		if transaction[0] != 'increment of PM2.5 = nan':
			if abs(incre_PM2_5) != 0.0 and abs(incre_temperature) != 0.0 and abs(incre_humidity) != 0.0:
				csv.writer(w).writerow(transaction)

		last = row