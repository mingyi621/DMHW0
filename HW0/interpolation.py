from scipy import interpolate
import csv
f = open('output4.csv','r')
w = open('output5.csv','w')

def timestamp(date, time):
	
	splitDate = date.split('-')
	intDate = int(splitDate[2])
	splitTime = time.split(':')
	intHour = int(splitTime[0])
	intMinute = int(splitTime[1])
	intSecond = int(splitTime[2])

	stamp = intDate * 86400 + intHour * 3600 + intMinute * 60 + intSecond * 1

	return stamp

def reverseTimestamp(stamp):
	second = stamp % 60
	stamp = stamp - second
	minute = (stamp % 3600) / 60
	stamp = stamp - minute * 60
	hour = (stamp % 86400) / 3600
	stamp = stamp - hour * 3600
	day = stamp / 86400

	date = '2017-03-' + str(day).zfill(2)
	time = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

	return date, time

print "Start interpolation."

x = []

start = 86400
target = start
end = 2764800

while target < 2764800:
	x.append(target)
	target = target + 900

t = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
sensor = ''
location = []

header = ['Date', 'Time', 'device_id', 'PM2.5', 'PM10', 'PM1', 'Temperature', 'Humidity', 'latitude', 'longitude']
csv.writer(w).writerow(header)

for row in csv.reader(f):
	if sensor != '' and sensor != row[2]:
		# do the interpolation
		print len(t),len(data1)
		g1 = interpolate.interp1d(t,data1, bounds_error=False)
		g2 = interpolate.interp1d(t,data2, bounds_error=False)
		g3 = interpolate.interp1d(t,data3, bounds_error=False)
		g4 = interpolate.interp1d(t,data4, bounds_error=False)
		g5 = interpolate.interp1d(t,data5, bounds_error=False)
		z1 = g1(x)
		z2 = g2(x)
		z3 = g3(x)
		z4 = g4(x)
		z5 = g5(x)

		for tt, uu1, uu2, uu3, uu4, uu5 in zip(x, z1, z2, z3, z4, z5):
			output = [reverseTimestamp(tt)[0],reverseTimestamp(tt)[1],sensor,round(uu1,0),round(uu2,0),round(uu3,0),round(uu4,2),round(uu5,0),location[0],location[1]]
			csv.writer(w).writerow(output)

		t = []
		data1 = []
		data2 = []
		data3 = []
		data4 = []
		data5 = []
	if sensor != row[2]:
		sensor = row[2]
		location = [row[8],row[9]]
	time = timestamp(row[0],row[1])
	t.append(time)
	data1.append(float(row[3]))
	data2.append(float(row[4]))
	data3.append(float(row[5]))
	data4.append(float(row[6]))
	data5.append(float(row[7]))

# do the last interpolation
print "The last interpolation:"
print len(t),len(data1)
g1 = interpolate.interp1d(t,data1, bounds_error=False)
g2 = interpolate.interp1d(t,data2, bounds_error=False)
g3 = interpolate.interp1d(t,data3, bounds_error=False)
g4 = interpolate.interp1d(t,data4, bounds_error=False)
g5 = interpolate.interp1d(t,data5, bounds_error=False)
z1 = g1(x)
z2 = g2(x)
z3 = g3(x)
z4 = g4(x)
z5 = g5(x)

for tt, uu1, uu2, uu3, uu4, uu5 in zip(x, z1, z2, z3, z4, z5):
	output = [reverseTimestamp(tt)[0],reverseTimestamp(tt)[1],sensor,round(uu1,0),round(uu2,0),round(uu3,0),round(uu4,2),round(uu5,0),location[0],location[1]]
	csv.writer(w).writerow(output)

print "The file has been outputed to output5.csv"