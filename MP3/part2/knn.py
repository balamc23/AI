from read_data import DataReader
import numpy as np
import time
import calendar
import time
class KNN:
	def __init__(self,input_num=3):
		
		self.reader = DataReader()
		self.train = list()
		self.success = []
		self.conf_matr = dict()
		for i in range(1,input_num):
			temp =[[0 for i in range(10)] for j in range(10)]
			self.conf_matr[i]=temp
		for i in range(1,input_num):
			self.knn(i)

		for i in range(1,input_num):
			for j in range(10):
				for k in range(10):
					self.conf_matr[i][j][k]=((self.conf_matr[i][j][k])/(len(self.reader.test_data[str(j)])))*100
		
		for i in range(1,input_num):
			print()
			print('for k as ', i)
			print('accuracy is ', (self.success[i-1]/444) * 100)
			print('the confusion matrix is ')
			print()
			for j in range(10):
				print(self.conf_matr[i][j])
			print()


	def knn(self, knum):
		succ = 0
		for i in self.reader.test_data.keys():
			# iterating through all 0-9
			
			print('currently testing ', i)
			cur_data = self.reader.test_data[i]
			# iterating through each number of each kind (0-9)
			for j in cur_data:
				cur = time.time()
				# print(j)
				distances = list()
				# iterating through all numbers in training dataset
				for k in self.reader.train_data.keys():
					# print('currently training on ', k)
					cur_train_data=self.reader.train_data[k]
					# iterating through and calc hamming 
					for l in cur_train_data:
						cur_distance = self.hamming(j,l)
						# k is the actual element its classified as (0-9)
						# print('the distance is ', cur_distance)
						# time.sleep(0.1)
						distances.append((cur_distance,k))
				# holds (hamming distance, (0-9))
				distances = sorted(distances, reverse = True)
				# selecting k top neighbors
				distances = distances[0:knum]
				cl=self.classifier(distances) 
				if (cl == int(i)):
					succ += 1
				self.conf_matr[knum][int(i)][int(cl)]+=1
				print("The elapsed time is ",time.time()-cur)
		self.success.append(succ)

	def classifier(self, arr):
		a = [0 for i in range(10)]
		for j in arr:
			a[int(j[1])] += 1
		max_val = -1
		for k in range(10):
			if a[k] > max_val:
				max_val = k
		print(max_val)		
		return max_val		

	def hamming(self, x, y):
		acc = 0
		for i in range(32):
			for j in range(32):
				if ((int(x[i][j]) - int(y[i][j])) == 0):
					acc+=1
		return acc


a = KNN()