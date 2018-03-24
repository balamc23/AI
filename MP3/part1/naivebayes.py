
import numpy as np
import math

k = 1

class NaiveBayes:

	def __init__(self):
		self.freq_table = np.zeros((10,32,32))
		self.probabs = np.zeros((10,32,32))
		self.train_count = np.zeros(10)




	def train(self, data_set):
		with open(data_set) as d:
			data_lines = d.readlines()
			for a in range (1,1+len(data_lines)//33):
				number = int(data_lines[33*a -1][1])
				self.train_count[number] = 1 + self.train_count[number]
				for i in range(32):
					for j in range(32):
						self.freq_table[number][i][j] += int(data_lines[i + 33*(a-1)][j])

		for n in range(10):
			for i in range(32):
				for j in range(32):
					self.probabs[n][i][j] =(k + self.freq_table[n][i][j] )/ (self.train_count[n] + 2*k)

	def test(self, data_set):
		correct = 0
		class_corr = np.zeros(10)
		incorrect = 0
		class_incorr = np.zeros(10)
		confusion = np.zeros((10,10))
		test_count = np.zeros(10)
		with open(data_set) as d:
			data_lines = d.readlines()
			for a in range (1,1+len(data_lines)//33):
				number = int(data_lines[33*a -1][1])
				test_count[number] +=1
				result =[]
				for n in range(10):
					P = math.log(0.1)
					for i in range(32):
						for j in range(32):
							if(self.probabs[n][i][j] * int(data_lines[33*(a-1)+i][j])  != 0):
								P = P + math.log(self.probabs[n][i][j] * int(data_lines[33*(a-1)+i][j]) )
					result.append((P,n))
				predict = max(result)[1]
				confusion[number][predict] += 1
				if(number == predict):
					correct += 1
					class_corr[number] +=1
				else:
					incorrect +=1
					class_incorr[number] +=1
				#print('Expected: ',number, 'Number is: ',max(result)[1])
			print('Correct: ',correct)
			print('Incorrect: ', incorrect)
			print('Accuracy: ', 100*correct/(correct+incorrect), '%')
			print('Classificaiton Accuracy for Each Digit')
			for n in range (10):
				print(n,':', 100 * class_corr[n]/(class_corr[n]+class_incorr[n]), '%' )
			print('     0      1      2      3      4      5      6      7      8      9')
			for i in range(10):
				print(i, end='| ')
				for j in range(10):
					confusion[i][j] = 100 * confusion[i][j] / test_count[i]
					if(confusion[i][j] < 10):
						print('0'+ "%.2f" % confusion[i][j], end = '| ')
					else:
						print("%.2f" % confusion[i][j], end = '| ')
				print()
			# print(confusion)




NB = NaiveBayes()
NB.train('digitdata/optdigits-orig_train.txt')
NB.test('digitdata/optdigits-orig_test.txt')


