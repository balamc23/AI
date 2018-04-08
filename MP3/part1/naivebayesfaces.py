import numpy as np
import math

k = 1

class NaiveBayesFaces:

	def __init__(self):		
		self.probabs = np.zeros((2,70,61))

	def train(self,train_set,train_label):
		labels = []
		freq_table = np.zeros((2,70,61))
		train_count = np.zeros(2)
		with open(train_label) as L:
			label_lines = L.readlines()
			labels = np.zeros(len(label_lines))
			i =0
			for a in label_lines:
				labels[i] = a[0]
				i += 1
		with open(train_set) as d:
			data_lines = d.readlines()
			idx = 0
			for a in range(len(data_lines)//70):
				idx = int(labels[a])
				train_count[idx] +=1
				for i in range(70):
					for j in range(61):
						if(data_lines[70*a +i][j] == '#'):
							freq_table[idx][i][j] += 1
		for n in range(2):
			for i in range(70):
				for j in range(61):
					self.probabs[n][i][j] = (k + freq_table[n][i][j])/ (train_count[n] +2*k)


	def test(self,test_set,test_label):
		labels = []
		correct = 0 
		class_corr = np.zeros(2)
		incorrect = 0 
		class_incorr = np.zeros(2)
		confusion = np.zeros((2,2))
		test_count = np.zeros(2)
		with open(test_label) as L:
			label_lines = L.readlines()
			labels = np.zeros(len(label_lines))
			i =0
			for a in label_lines:
				labels[i] = a[0]
				i += 1
		with open(test_set) as d:
			data_lines = d.readlines()
			idx = 0
			for a in range(len(data_lines)// 70 ):
				idx = int(labels[a])
				test_count[idx] += 1
				result = []
				for n in range(2):
					P = math.log(1)
					for i in range(70):
						for j in range(61):
							if(data_lines[70*a +i][j] == '#'):
								P = P + math.log(self.probabs[n][i][j])
					result.append((P,n))
				predict = max(result)[1]
				confusion[idx][predict] += 1
				if(idx == predict):
					print(a, result)
					correct += 1
					class_corr[idx] += 1
				else:
					# print(a, result)
					incorrect += 1
					class_incorr[idx] += 1
		print('Correct: ',correct)
		print('Incorrect: ', incorrect)
		print('Accuracy: ', 100*correct/(correct+incorrect), '%')
		print('Classificaiton Accuracy for Each Digit')
		for n in range (2):
			print(n,':', 100 * class_corr[n]/(class_corr[n]+class_incorr[n]), '%' )	
		print('     0      1      2      ')
		for i in range(2):
			print(i, end='| ')
			for j in range(2):
				confusion[i][j] = 100 * confusion[i][j] / test_count[i]
				if(confusion[i][j] < 10):
					print('0'+ "%.2f" % confusion[i][j], end = '| ')
				else:
					print("%.2f" % confusion[i][j], end = '| ')
			print()

		


F = NaiveBayesFaces()
F.train('facedata/facedata/facedatatrain','facedata/facedata/facedatatrainlabels')
F.test('facedata/facedata/facedatatest','facedata/facedata/facedatatestlabels')