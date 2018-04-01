from read_data import DataReader
import numpy as np

class Perceptron:
	def __init__(self):
		self.weights = dict()
		for i in range(10):
			self.weights[i] = list(np.random.random((32,32)))
			# print(self.weights[i])
		self.reader = DataReader()
		self.n = 0.1
		self.train()
		self.test()
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
			print('',i,value)
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

	def test(self):
		for i in self.reader.test_data.keys():
			# iterating through all 0-9
			cur_data = self.reader.test_data[i]
			# iterating through each number of each kind (0-9)
			for j in cur_data:
				ret = self.classifier(j)
				print('testing ', i, ret)
				if ret == int(i):
					print('xxx')


a = Perceptron()
