import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

kmeans = KMeans(n_clusters=3).fit(locations)
labels = kmeans.labels_

lat0 = []
lot0 = []
lat1 = []
lot1 = []
lat2 = []
lot2 = []
for la,lo,col in zip(lat,lot,labels):
	if col == 0:
		lat0.append(la)
		lot0.append(lo)
	elif col == 1:
		lat1.append(la)
		lot1.append(lo)
	else:
		lat2.append(la)
		lot2.append(lo)

plt.scatter(lot0,lat0,color='red')
plt.scatter(lot1,lat1,color='blue')
plt.scatter(lot2,lat2,color='green')
plt.show()


