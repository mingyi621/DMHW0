from scipy import interpolate
import csv

f = open('oneSensorOrigin.csv','r')
w = open('oneSensorInterpolated.csv','w')

def timestamp(date, time):
	
	splitDate = date.split('-')
	intMonth = int(splitDate[1])
	intDate = int(splitDate[2])
	splitTime = time.split(':')
	intHour = int(splitTime[0])
	intMinute = int(splitTime[1])
	intSecond = int(splitTime[2])

	if intMonth == 1:
		stamp = intDate * 86400 + intHour * 3600 + intMinute * 60 + intSecond * 1
	elif intMonth == 2:
		stamp = 31*24*60*60 + intDate * 86400 + intHour * 3600 + intMinute * 60 + intSecond * 1
	elif intMonth == 3:
		stamp = (31+28)*24*60*60 + intDate * 86400 + intHour * 3600 + intMinute * 60 + intSecond * 1
	else:
		print 'Something is wrong.'
	return stamp

def reverseTimestamp(stamp):
	second = stamp % 60
	stamp = stamp - second
	minute = (stamp % 3600) / 60
	stamp = stamp - minute * 60
	hour = (stamp % 86400) / 3600
	stamp = stamp - hour * 3600
	day = stamp / 86400
	if day <= 31:
		month = 1
	elif day > 31 and day <= 31 + 28:
		month = 2
		day = day - 31
	elif day > 31 + 28:
		month = 3
		day = day - (31+28)
	else:
		print 'Something is wrong.'


	date = '2017-' + str(month).zfill(2) + '-' + str(day).zfill(2)
	time = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)

	return date, time

print "Start interpolation."

x = []

t = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
sensor = '74DA3895DFB8'
location = [23.286,120.138]

start = 86400
target = start
end = 86400 + (31 + 28 + 31) * 86400

while target < 86400 + (31 + 28 + 31) * 86400:
	x.append(target)
	target = target + 900

for row in csv.reader(f):
	time = timestamp(row[0],row[1])
	t.append(time)
	data1.append(float(row[3]))
	data2.append(float(row[4]))
	data3.append(float(row[5]))
	data4.append(float(row[6]))
	data5.append(float(row[7]))

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

print "The file has been outputed to oneSensorInterpolated.csv"






