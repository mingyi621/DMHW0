# AgglomerativeClustering
import csv
from sklearn.cluster import AgglomerativeClustering as Agg
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
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
		data.append(row[6]) # The temperature Record
dataSet.append(data)

sensors = []
lat = []
lot = []
for row in csv.reader(g):
	sensors.append(row[2])
	lat.append(row[8])
	lot.append(row[9])

agg = Agg(n_clusters=5).fit(dataSet)
labels = agg.labels_

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

plt.show()

plt.gcf().clear()

pca = PCA(n_components = 3)
newDataSet = pca.fit_transform(dataSet)
'''
temp = []
for element in newDataSet:
	temp.append(element/500)
newDataSet = temp
'''
agg = Agg(n_clusters=5).fit(newDataSet)
labels = agg.labels_

fig = plt.figure()
Axes3D = fig.add_subplot(111, projection='3d')


for la,lo,d,lab in zip(lat,lot,newDataSet,labels):
	if lab == 0:
		Axes3D.scatter(d[0],d[1],d[2],color='red')
	elif lab == 1:
		Axes3D.scatter(d[0],d[1],d[2],color='yellow')
	elif lab == 2:
		Axes3D.scatter(d[0],d[1],d[2],color='blue')
	elif lab == 3:
		Axes3D.scatter(d[0],d[1],d[2],color='orange')
	elif lab == 4:
		Axes3D.scatter(d[0],d[1],d[2],color='green')	
#	elif lab == 5:
#		Axes3D.scatter(lo,la,d,color='black')		
#	elif lab == -1:
#		Axes3D.scatter(lo,la,d,color='red')
	else:
		print 'hello'

plt.show()




