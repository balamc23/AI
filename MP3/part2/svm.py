from read_data import DataReader
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

a=DataReader()
x_train=list()
y_train=list()
for i in a.train_data.keys():
	for j in a.train_data[i]:
		x_train.append(j)
		y_train.append(int(i))
		# print(int(i))

x_train_flat = list()
for i in x_train:
	temp = list()
	for j in i:
		temp.append(j)
	x_train_flat.append(temp)

x_test=list()
y_test=list()

for i in a.test_data.keys():
	for j in a.test_data[i]:
		x_test.append(j)
		y_test.append(int(i))

x_test_flat = list()
for i in x_test:
	temp = list()
	for j in i:
		temp.append(j)
	x_test_flat.append(temp)

# clf = svm.SVC()
clf = KNeighborsClassifier(n_neighbors = 3)
clf.fit(x_train_flat, y_train)
pred = clf.predict(x_test_flat)

acc = accuracy_score(y_test, pred)
print(acc)

