
import numpy as np
import math
import plotly as py
import plotly.graph_objs as go

k = 1
MAPS = []

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
		max_map = np.zeros(10)
		max_num = np.zeros(10)
		min_map = np.zeros(10)
		min_num = np.zeros(10)
		for i in range (10):
			max_map[i] = -100000000000
			min_map[i] =  100000000000

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
				prob, predict = max(result)
				if(prob > max_map[predict]):
					max_map[predict] = prob
					max_num[predict] = a
				if(prob < min_map[predict]):
					min_map[predict] = prob
					min_num[predict] = a

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
			for n in range(10):
				MAPS.append(min_num[n])
				MAPS.append(max_num[n])
				print('Max MAP for',n,':', max_map[n],' token num:',max_num[n])
				print('Min MAP for',n,':', min_map[n],' token num:',min_num[n])

			# print_MAPS(data_set)


			# #Odss Ratios
			
			# # (wrong - right) 8- 2 ,  9 -5, 7- 4,  9-3 
			# log_prob = np.zeros((10,32,32))
			# for n in range(10):
			# 	for i in range(32):
			# 		for j in range(32):
			# 			log_prob[n][i][j] = math.log10(self.probabs_one[n][i][j])

			# # 8- 2
			# trace = go.Heatmap(z = log_prob[8])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '8.html')

			# trace = go.Heatmap(z = log_prob[2])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '2.html')

			# odds = np.zeros((32,32))
			# for i in range (32):
			# 	for j in range(32):
			# 		odds[i][j] = math.log10(self.probabs_one[8][i][j] / self.probabs_one[2][i][j])
					

			# trace = go.Heatmap(z = odds)
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = 'EightbyTwo.html')			

			# # 9- 5
			
			# trace = go.Heatmap(z = log_prob[5])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '5.html')

			# odds = np.zeros((32,32))
			# for i in range (32):
			# 	for j in range(32):
			# 		odds[i][j] = math.log10(self.probabs_one[9][i][j] / self.probabs_one[5][i][j])
			# 		# odds[i][j] = log_prob[9][i][j]/ log_prob[5][i][j]

			# trace = go.Heatmap(z = odds)
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = 'NinebyFive.html')	

			# # 7- 4
			# trace = go.Heatmap(z = log_prob[7])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '7.html')

			# trace = go.Heatmap(z = log_prob[4])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '4.html')

			# odds = np.zeros((32,32))
			# for i in range (32):
			# 	for j in range(32):
			# 		odds[i][j] = math.log10(self.probabs_one[7][i][j] / self.probabs_one[4][i][j])
			# 		# odds[i][j] = log_prob[7][i][j]/ log_prob[4][i][j]

			# trace = go.Heatmap(z = odds)
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = 'SevenbyFour.html')	

			# # 9- 3
			# trace = go.Heatmap(z = log_prob[3])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '3.html')

			# trace = go.Heatmap(z = log_prob[9])
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = '9.html')

			# odds = np.zeros((32,32))
			# for i in range (32):
			# 	for j in range(32):
			# 		odds[i][j] = math.log10(self.probabs_one[9][i][j] / self.probabs_one[3][i][j])
			# 		# odds[i][j] = log_prob[9][i][j]/ log_prob[3][i][j]

			# trace = go.Heatmap(z = odds)
			# data = [trace]
			# layout = go.Layout( yaxis = dict(autorange='reversed'))
			# fig = go.Figure(data = data, layout = layout)
			# py.offline.plot(fig, filename = 'NinetbyThree.html')


def print_MAPS(data_set):
	with open(data_set) as d:
		data_lines = d.readlines()
		for n in range(10):
			a = MAPS[2*n]
			print('Min MAP for ',n,":")
			for i in range(32):
				for j in range(32):
					print(data_lines[int(33*(a-1)+i)][j],end ='')
				print()
			print()
			a = MAPS[2*n +1]
			print('Max MAP for ',n,":")
			for i in range(32):
				for j in range(32):
					print(data_lines[int(33*(a-1)+i)][j],end ='')
				print()
			print()



NB = NaiveBayes()
NB.train('digitdata/optdigits-orig_train.txt')
NB.test('digitdata/optdigits-orig_test.txt')



