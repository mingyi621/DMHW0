import csv
import time

f = open('oneSensorInterpolated.csv','r')

def catagory(num):
	result = 0
	num = float(num)
	if num <= 25:
		result = 1
	elif num <= 50:
		result = 2
	elif num <= 75:
		result = 3
	elif num <= 100:
		result = 4
	return result

def split(X, percent):
	num = len(X)
	numTraining = num * percent
	X_training = []
	X_test = []
	count = 0
	while count < len(X):
		if count < numTraining:
			X_training.append(X[count])
		else:
			X_test.append(X[count])
		count = count + 1
	return X_training, X_test

def evaluation(Y_test,Y_result):
	count = 0
	length = len(Y_test)
	for test, result in zip(Y_test,Y_result):
		if test == result:
			count = count + 1
	return str(count) + ' / ' + str(length) + ' = ' + str(round(float(count) * 100 / float(length),2)) + '%'

def transToInt(data):
	result = []
	for element in data:
		result.append(int(element))
	return result

data = []
for row in csv.reader(f):
	if row[3] != 'nan':
		data.append(row)

print 'The length of data = ' + str(len(data))

training = []
index = 0
while index <= len(data) - 8:
	line = [['','','','','','','','','','','',''],'']
	line[0][0] = float(data[index + 0][3])	# PM2.5
	line[0][1] = float(data[index + 1][3])	# PM2.5
	line[0][2] = float(data[index + 2][3])	# PM2.5
	line[0][3] = float(data[index + 3][3])	# PM2.5

	line[0][4] = float(data[index + 0][4])  # PM10
	line[0][5] = float(data[index + 1][4])  # PM10
	line[0][6] = float(data[index + 2][4])	# PM10
	line[0][7] = float(data[index + 3][4])	# PM10

	line[0][8] = float(data[index + 0][5])	# PM1
	line[0][9] = float(data[index + 1][5])	# PM1
	line[0][10]= float(data[index + 2][5])	# PM1
	line[0][11]= float(data[index + 3][5])	# PM1

	line[1] = catagory(data[index + 7][3])
	training.append(line)
	index = index + 1

# Start to classify
X = []
Y = []
for element in training:
	X.append(element[0])
	Y.append(element[1])

# Split the data
X_training, X_test = split(X, 0.7)
Y_training, Y_test = split(Y, 0.7)

# Using KNN classifier
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5)
time_start = time.clock()
neigh.fit(X_training, Y_training) 

Y_result = neigh.predict(X_test)	
print 'The time elasped of KNN classifier = ' + str(time.clock() - time_start)
Y_result = transToInt(Y_result)
print 'The evaluation of KNN classifier = ' + str(evaluation(Y_test, Y_result))
#print 'The precision_score of KNN classifier = ' + str(precision_score(Y_test, Y_result,average='macro'))
print ''

# Using Gaussian Naive Bayes Classifier
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Gaussian Naive Bayes Classifier = ' + str(time.clock() - time_start)
Y_result = transToInt(Y_result)
print 'The evaluation of Gaussian Naive Bayes Classifier = ' + str(evaluation(Y_test, Y_result))
print ''

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(max_depth=2, random_state=0)
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Random Forest Classifier = ' + str(time.clock() - time_start)
Y_result = transToInt(Y_result)
print 'The evaluation of Random Forest Classifier = ' + str(evaluation(Y_test, Y_result))
print ''

# Support Vector Machine
from sklearn import svm

clf = svm.SVC()
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Support Vector Machine Classifier = ' + str(time.clock() - time_start)
Y_result = transToInt(Y_result)
print 'The evaluation of Support Vector Machine Classifier = ' + str(evaluation(Y_test, Y_result))
print ''

# Neural Network
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Neural Network Classifier = ' + str(time.clock() - time_start)
Y_result = transToInt(Y_result)
print 'The evaluation of Neural Network Classifier = ' + str(evaluation(Y_test, Y_result))
print ''