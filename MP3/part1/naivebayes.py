
import numpy as np
import math
import plotly as py
import plotly.graph_objs as go

k = 1

class NaiveBayes:

	def __init__(self):
		self.freq_table_one = np.zeros((10,32,32))
		self.freq_table_zero = np.zeros((10,32,32))
		self.probabs_one = np.zeros((10,32,32))
		self.probabs_zero = np.zeros((10,32,32))
		self.train_count = np.zeros(10)


	def train(self, data_set):
		with open(data_set) as d:
			data_lines = d.readlines()
			for a in range (1,1+len(data_lines)//33):
				number = int(data_lines[33*a -1][1])
				self.train_count[number] = 1 + self.train_count[number]
				for i in range(32):
					for j in range(32):
						if(int(data_lines[i + 33*(a-1)][j]) == 1):
							self.freq_table_one[number][i][j] += 1
						else:
							self.freq_table_zero[number][i][j] += 1

		for n in range(10):
			for i in range(32):
				for j in range(32):
					self.probabs_one[n][i][j] =(k + self.freq_table_one[n][i][j] )/ (self.train_count[n] + 2*k)
					self.probabs_zero[n][i][j] =(k + self.freq_table_zero[n][i][j] )/ (self.train_count[n] + 2*k)

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
					P = math.log10(0.1)
					for i in range(32):
						for j in range(32):
							if(int(data_lines[33*(a-1)+i][j])  ==1 ):
								P = P + math.log10(self.probabs_one[n][i][j])
							else:
								P = P + math.log10(self.probabs_zero[n][i][j])
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

			#Odss Ratios
			# (wrong - right) 8- 2 ,  7 -4, 8- 4,  3-9 
			log_prob = np.zeros((10,32,32))
			for n in range(10):
				for i in range(32):
					for j in range(32):
						log_prob[n][i][j] = math.log10(self.probabs_one[n][i][j])

			# 8- 2
			trace = go.Heatmap(z = log_prob[8])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '8.html')

			trace = go.Heatmap(z = log_prob[2])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '2.html')

			odds = np.zeros((32,32))
			for i in range (32):
				for j in range(32):
					odds[i][j] = math.log10(self.probabs_one[8][i][j] / self.probabs_one[2][i][j])
					

			trace = go.Heatmap(z = odds)
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = 'EightbyTwo.html')			

			# 8- 4
			trace = go.Heatmap(z = log_prob[4])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '4.html')

			odds = np.zeros((32,32))
			for i in range (32):
				for j in range(32):
					odds[i][j] = math.log10(self.probabs_one[8][i][j] / self.probabs_one[4][i][j])
					# odds[i][j] = log_prob[8][i][j]/ log_prob[4][i][j]

			trace = go.Heatmap(z = odds)
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = 'EightbyFour.html')	

			# 7- 4
			trace = go.Heatmap(z = log_prob[7])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '7.html')

			odds = np.zeros((32,32))
			for i in range (32):
				for j in range(32):
					odds[i][j] = math.log10(self.probabs_one[7][i][j] / self.probabs_one[4][i][j])
					# odds[i][j] = log_prob[7][i][j]/ log_prob[4][i][j]

			trace = go.Heatmap(z = odds)
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = 'SevenbyFour.html')	

			# 3- 9
			trace = go.Heatmap(z = log_prob[3])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '3.html')

			trace = go.Heatmap(z = log_prob[9])
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = '9.html')

			odds = np.zeros((32,32))
			for i in range (32):
				for j in range(32):
					odds[i][j] = math.log10(self.probabs_one[3][i][j] / self.probabs_one[9][i][j])
					# odds[i][j] = log_prob[3][i][j]/ log_prob[9][i][j]

			trace = go.Heatmap(z = odds)
			data = [trace]
			layout = go.Layout( yaxis = dict(autorange='reversed'))
			fig = go.Figure(data = data, layout = layout)
			py.offline.plot(fig, filename = 'ThreetbyNine.html')





NB = NaiveBayes()
NB.train('digitdata/optdigits-orig_train.txt')
NB.test('digitdata/optdigits-orig_test.txt')


