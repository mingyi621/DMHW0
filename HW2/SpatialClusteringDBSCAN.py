import csv
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np

f = open('location_modified.csv','r')

next(csv.reader(f))
locations = []
spot = []
lat = []
lot = []

for row in csv.reader(f):
	spot = [row[9],row[8]]
	locations.append(spot)
	lat.append(row[8])
	lot.append(row[9])

db = DBSCAN(eps=0.14, min_samples=4).fit(locations)
db = DBSCAN(eps=0.25, min_samples=4).fit(locations)

min = 0
for number in db.labels_:
	if number > min:
		min = number
#	if number == -1:
#		print number
print min

labels = db.labels_

lat_1 = []
lot_1 = []
lat0 = []
lot0 = []
lat1 = []
lot1 = []
lat2 = []
lot2 = []
lat3 = []
lot3 = []
lat4 = []
lot4 = []

for la,lo,col in zip(lat,lot,labels):
	if col == -1:
		lat_1.append(la)
		lot_1.append(lo)
	elif col == 0:
		lat0.append(la)
		lot0.append(lo)
	elif col == 1:
		lat1.append(la)
		lot1.append(lo)
	elif col == 2:
		lat2.append(la)
		lot2.append(lo)
	elif col == 3:
		lat3.append(la)
		lot3.append(lo)
	else:
		lat4.append(la)
		lot4.append(lo)

plt.scatter(lot_1,lat_1,color='red')
plt.scatter(lot0,lat0,color='green')
plt.scatter(lot1,lat1,color='blue')
plt.scatter(lot2,lat2,color='yellow')
plt.scatter(lot3,lat3,color='brown')
plt.scatter(lot4,lat4,color='purple')
plt.show()
