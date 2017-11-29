#Using DBSCAN
import csv
import matplotlib.pyplot as plt
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np

def MaxMinNormalization(x,Max,Min): 
	x = (x - Min) / (Max - Min); 
	return x;

def findMax(array):
	i = array[0]
	for element in array:
		if element > i:
			i = element
	return i

def findMin(array):
	i = array[0]
	for element in array:
		if element < i:
			i = element
	return i

f = open('input.csv','r')
#w = open('output1.csv')


next(csv.reader(f))

lat = []
lot = []
PM2_5 = []

for row in csv.reader(f):
	if row[0] == '2017-03-10' and row[1] == '17:15:00':
#		csv.writer(w).writerow(row)
		lat.append(float(row[8]))
		lot.append(float(row[9]))
		PM2_5.append(float(row[3]))

#plt.scatter(lot,lat,PM2_5)
#plt.show()
''' 
all_spots = []
for la,lo,pm in zip(lat,lot,PM2_5):
	all_spots.append([la,lo,pm])

all_spots = np.array(all_spots)
all_spots = preprocessing.normalize(all_spots)
'''

lat_n = []
lot_n = []
PM2_5_n = []
'''
for e in all_spots:
	lat_n.append(e[0])
	lot_n.append(e[1])
	PM2_5_n.append(e[2])
'''
latMax = findMax(lat)
latMin = findMin(lat)
lotMax = findMax(lot)
lotMin = findMin(lot)
PM2_5Max = findMax(PM2_5)
PM2_5Min = findMin(PM2_5)
i = 0
while i < len(lat):
	lat_n.append(MaxMinNormalization(lat[i],latMax,latMin))
	lot_n.append(MaxMinNormalization(lot[i],lotMax,lotMin))
	PM2_5_n.append(MaxMinNormalization(PM2_5[i],PM2_5Max,PM2_5Min))
	i = i + 1


fig = plt.figure()
Axes3D = fig.add_subplot(111, projection='3d')

#Axes3D.scatter(lot_n,lat_n,PM2_5_n)
#Axes3D.scatter(lot,lat,PM2_5)
#plt.scatter(lot_n,lat_n)
#plt.show()

all_spots = []
for la,lo,pm in zip(lat,lot,PM2_5):
	all_spots.append([la,lo,pm])

all_spots_n = []
for la,lo,pm in zip(lat_n,lot_n,PM2_5_n):
	all_spots_n.append([la,lo,pm])

#all_spots_n = np.array(all_spots_n)
#kmeans = KMeans(n_clusters=3).fit(all_spots_n)
#labels = kmeans.labels_
#db = DBSCAN(eps=4, min_samples=5).fit(all_spots)
db = DBSCAN(eps=0.15, min_samples=5).fit(all_spots_n)
labels = db.labels_

min = 0
for number in labels:
	if number > min:
		min = number
	if number == -1:
		print number
print min

for la,lo,pm,col in zip(lat_n,lot_n,PM2_5_n,labels):
	if col == 0:
		Axes3D.scatter(lo,la,pm,color='yellow')
	elif col == 1:
		Axes3D.scatter(lo,la,pm,color='green')
	elif col == 2:
		Axes3D.scatter(lo,la,pm,color='blue')
	elif col == 3:
		Axes3D.scatter(lo,la,pm,color='brown')
	elif col == 4:
		Axes3D.scatter(lo,la,pm,color='purple')	
	elif col == 5:
		Axes3D.scatter(lo,la,pm,color='black')		
	elif col == -1:
		Axes3D.scatter(lo,la,pm,color='red')
	else:
		print 'hello'

plt.show()


