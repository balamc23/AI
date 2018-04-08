from read_data import DataReader
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
	def __init__(self,epochs=2):
		# randomize weight vectors
		self.weights = dict()
		for i in range(10):
			self.weights[i] = list(np.random.random((32,32)))
			# print(self.weights[i])
		self.reader = DataReader()
		self.n = 0.1
		accs=list()
		self.conf_matrices={}
		for k in range(epochs):
			self.conf_matrices[k]=[[0 for i in range(10)] for j in range(10)]
		# epochs, # of passes through training data			
		for j in range(epochs):
			self.train()
			accs.append(((self.test(j))/444)*100)
		max_ep = 0
		mx_acc = 0
		for i in range(epochs):
			for j in range(10):
				for k in range(10):
					self.conf_matrices[i][j][k]=((self.conf_matrices[i][j][k])/(len(self.reader.test_data[str(j)])))*100

		for k in range(len(accs)):
			if accs[k]>mx_acc:
				mx_acc=accs[k]
				max_ep=k
		print('max accuracy for test set: ', mx_acc," for no of epochs = ",max_ep)
		plt.plot([(i+1) for i in range(epochs)],accs,'r--')
		plt.show()

		for l in range(epochs):
			print("The accuracy for the epoch ",l+1," is ",accs[l])
			print("the conf matrix is")
			cur_arrr = self.conf_matrices[l]
			for m in cur_arrr:
				for n in m:
					print("%.2f"%n,end="  ")
				print()
		# for i in range(10):
		# 	for j in self.weights[i]:
		# 		print(j)
		# 	print()
	
	def train(self):
		# iterating through all numbers in training dataset
		for i in self.reader.train_data.keys():
			# print('currently training on ', k)
			cur_train_data = self.reader.train_data[i]
			# j holds 32x32 for one number
			for j in cur_train_data:
				ret = self.classifier(j)
				if ret != int(i):
					self.update(int(i),j)

	def update(self, num, matr):
		for i in range(32):
			for j in range(32):
				self.weights[num][i][j] += float(self.n) * float(matr[i][j])

	def classifier(self, arr):
		m = -1
		cl = 0
		for i in range(10):
			value = self.mult(arr, self.weights[i])
			# print('',i,value)
			if value > m:
				m = value
				cl = i
		return cl

	def mult(self, x,y):
		acc = 0
		for i in range(32):
			for j in range(32):
				acc += float(x[i][j]) * float(y[i][j])
		return acc

	def test(self,epoch_no):
		acc=0
		for i in self.reader.test_data.keys():
			# iterating through all 0-9
			cur_data = self.reader.test_data[i]
			# iterating through each number of each kind (0-9)
			for j in cur_data:
				ret = self.classifier(j)
				print('testing ', i, ret)
				if ret == int(i):
					acc+=1
				self.conf_matrices[epoch_no][int(i)][ret]+=1
		print(acc)
		return acc
					


a = Perceptron()
