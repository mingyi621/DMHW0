import csv
import time
from sklearn.metrics import explained_variance_score
f = open('oneSensorInterpolated.csv','r')

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

data = []
for row in csv.reader(f):
	if row[3] != 'nan':
		data.append(row)

print 'The length of data = ' + str(len(data))

training = []
index = 0
while index <= len(data) - 8:
	line = ['','','','','']
	line[0] = float(data[index][3])
	line[1] = float(data[index + 1][3])
	line[2] = float(data[index + 2][3])
	line[3] = float(data[index + 3][3])
	line[4] = float(data[index + 7][3]) # Regression doesn't need to categorize.
	training.append(line)
	index = index + 1

X = []
Y = []
for element in training:
	line = [element[0],element[1],element[2],element[3]]
	X.append(line)
	Y.append(element[4])

# Split the data
X_training, X_test = split(X, 0.7)
Y_training, Y_test = split(Y, 0.7)

# Baysian Linear Regression
from sklearn import linear_model

clf = linear_model.BayesianRidge()
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Baysian Linear Regression = ' + str(time.clock() - time_start)
print 'The evaluation of Baysian Linear Regression = ' + str(explained_variance_score(Y_test, Y_result))

# Decision Tree Regressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=2)
time_start = time.clock()
regr_1.fit(X_training, Y_training)

Y_result = regr_1.predict(X_test)
print 'The time elasped of Decision Tree Regression = ' + str(time.clock() - time_start)
print 'The evaluation of Decision Tree Regression = ' + str(explained_variance_score(Y_test, Y_result))

# Support Vector Regression
from sklearn.svm import SVR
clf = SVR(C=1.0, epsilon=0.1)
time_start = time.clock()
clf.fit(X_training, Y_training)

Y_result = clf.predict(X_test)
print 'The time elasped of Support Vector Regression = ' + str(time.clock() - time_start)
print 'The evaluation of Support Vector Regression = ' + str(explained_variance_score(Y_test, Y_result))

# Linear Regression
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
time_start = time.clock()
lm.fit(X_training, Y_training)

Y_result = lm.predict(X_test)
print 'The time elasped of Linear Regression = ' + str(time.clock() - time_start)
print 'The evaluation of Linear Regression = ' + str(explained_variance_score(Y_test, Y_result))
