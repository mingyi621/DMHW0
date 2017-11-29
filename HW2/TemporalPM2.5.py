#KMeans
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

f = open('input.csv','r')
g = open('location_modified.csv','r')
date = '2017-03-10'

next(csv.reader(f))

currentSensor = ''
dataSet = []
data = []
for row in csv.reader(f):
	if date == row[0]:
		if row[2] != currentSensor and currentSensor != '':
			dataSet.append(data)
			data = []
		currentSensor = row[2]
		data.append(row[3])
dataSet.append(data)

sensors = []
lat = []
lot = []
for row in csv.reader(g):
	sensors.append(row[2])
	lat.append(row[8])
	lot.append(row[9])

kmeans = KMeans(n_clusters=6).fit(dataSet)
labels = kmeans.labels_
'''
for s,d,l,la,lo in zip(sensors,dataSet,labels,lat,lot):
	if l == 0:
		plt.scatter(lo,la,color='red')
	elif l == 1:
		plt.scatter(lo,la,color='yellow')
	elif l == 2:
		plt.scatter(lo,la,color='blue')
	elif l == 3:
		plt.scatter(lo,la,color='orange')
	elif l == 4:
		plt.scatter(lo,la,color='green')
	elif l == 5:
		plt.scatter(lo,la,color='brown')
	else:
		print 'hello'
'''
#plt.show()

pca = PCA(n_components = 3)
newDataSet = pca.fit_transform(dataSet)

#fig = plt.figure()
#Axes3D = fig.add_subplot(111, projection='3d')

kmeans = KMeans(n_clusters = 6).fit(newDataSet)
labels = kmeans.labels_

for s,d,l,la,lo in zip(sensors,newDataSet,labels,lat,lot):
	if l == 0:
		plt.scatter(lo,la,color='red')
	elif l == 1:
		plt.scatter(lo,la,color='yellow')
	elif l == 2:
		plt.scatter(lo,la,color='blue')
	elif l == 3:
		plt.scatter(lo,la,color='orange')
	elif l == 4:
		plt.scatter(lo,la,color='green')
	elif l == 5:
		plt.scatter(lo,la,color='brown')
	else:
		print 'hello'

plt.show()

