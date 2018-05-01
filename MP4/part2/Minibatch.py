import numpy as np 
import helpers as h
from progress import printProgressBar
import copy
import matplotlib.pyplot as plt
from game_env import MarkovDecisionProcess as MDP
import pickle


class DeepPong:
	def __init__(self):
		self.data = np.array((self.readData('expert_policy.txt')))
		self.stats = np.zeros((5,2))
		self.Normalize()
		self.mdp = MDP()
		self.W1 = np.random.uniform(-0.1,0.1,(5,256))
		self.W2 = np.random.uniform(-0.1,0.1,(256,256))
		self.W3 = np.random.uniform(-0.1,0.1,(256,256))
		self.W4 = np.random.uniform(-0.1,0.1,(256,3))
		self.b1 = np.zeros(256)
		self.b2 = np.zeros(256)		
		self.b3 = np.zeros(256)
		self.b4 = np.zeros(3)
		self.learning_rate = 0.1
		self.epoch_plot = []
		self.accuracy_plot = []
		self.loss_plot = []
		self.confusion = np.zeros((3,3))

	def Normalize(self):
		data_temp = copy.deepcopy(self.data)
		data_temp = np.transpose(data_temp)
		#0 for mean, 1 for std dev
		
		for i in range(5):
			self.stats[i][0] = np.mean(data_temp)
			self.stats[i][1] = np.std(data_temp)
		for j in range(len(self.data[0])-1):
			for i in range(len(self.data)):
				self.data[i][j] = (self.data[i][j]-self.stats[j][0])/ self.stats[j][1]


	def readData(self,dataFile):
		with open(dataFile) as df:
			d_r = df.readlines()
			data = np.zeros((len(d_r), 6))
			i =0
			for line in d_r:
				string =''
				j = 0	
				for h in range(len(line)):
					if(line[h] == ' ' or line[h] == '\n'):
						data[i][j] = float(string)
						string =''
						j += 1
					else:
						string += line[h]
				i += 1
				
		return data	

	def FourLayerNetwork(self,X,W1,W2,W3,W4,b1,b2,b3,b4,y,test,n):
		Z1,acache1 = h.Affine_Forward(X,W1,b1)
		# print("Affine 1 Done")
		A1,rcache1 = h.ReLu_Forward(Z1)
		Z2,acache2 = h.Affine_Forward(A1,W2,b2)
		# print("Affine 2 Done")
		A2,rcache2 = h.ReLu_Forward(Z2)
		Z3,acache3 = h.Affine_Forward(A2,W3,b3)
		# print("Affine 3 Done")
		A3,rcache3 = h.ReLu_Forward(Z3)
		F,acache4  = h.Affine_Forward(A3,W4,b4)		
		# print("Affine 4 Done")

		if(test == 1):
			classification = int(np.argmax(F))
			return classification

		loss, dF = h.Cross_Entropy(F, y, n)
		# print("Entropy Done")
		dA3, dW4, dB4 = h.Affine_Backward(dF, acache4)
		# print("Affine_b 1 Done")
		dZ3 = h.ReLu_Backward(dA3, rcache3)
		dA2, dW3, dB3 = h.Affine_Backward(dZ3, acache3)
		# print("Affine_b 2 Done")
		dZ2 = h.ReLu_Backward(dA2, rcache2)
		dA1, dW2, dB2 = h.Affine_Backward(dZ2, acache2)
		# print("Affine_b 3 Done")
		dZ1 = h.ReLu_Backward(dA1, rcache1)
		dX, dW1, dB1 = h.Affine_Backward(dZ1, acache1)
		# print("Affine_b 4 Done")
		
		self.W1 = self.W1 - self.learning_rate * dW1
		self.W2 = self.W2 - self.learning_rate * dW2
		self.W3 = self.W3 - self.learning_rate * dW3
		self.W4 = self.W4 - self.learning_rate * dW4

		self.b1 = self.b1 - self.learning_rate*dB1
		self.b2 = self.b2 - self.learning_rate*dB2
		self.b3 = self.b3 - self.learning_rate*dB3
		self.b4 = self.b4 - self.learning_rate*dB4
		return loss



	def MiniBatchGD(self,Epochs):
		self.data = np.array(self.data)
		N = 10000
		n = 128
		num_of_y = np.zeros(3)
		printProgressBar(0, Epochs-1, prefix = 'Training:', suffix = 'Complete', length = 50)
		for e in range(Epochs):
			np.random.shuffle(self.data)
			printProgressBar(e, Epochs-1, prefix = 'Training:', suffix = 'Complete', length = 50)
			for j in range(0,N//n):
				A = []
				y = []
				for i in range(j*n,j*n+n):				
					A.append(self.data[i][:5])
					y.append(self.data[i][5])
				A = np.array(A)
				y = np.array(y)			

				loss = self.FourLayerNetwork(A, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, 0,n)

			if(e%25 == 0 or e == Epochs-1):
				np.random.shuffle(self.data)
				correct = 0
				
				for i in range(N):
					A = self.data[i][:5]
					y = self.data[i][5]
					A = np.array(A)
					
					classification = self.FourLayerNetwork(A, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, 1,n)
					
					if(e == Epochs-1):
						y = int(y)
						num_of_y[y] +=1
						self.confusion[y][classification] += 1
					if(classification == y):
						correct += 1

				accuracy = 100 *  correct / N
				self.epoch_plot.append(e)
				self.accuracy_plot.append(accuracy)
				self.loss_plot.append(loss)
				print()
				print('Accuracy: ', accuracy, '%')

		#confusion matrix	
		print('Confusion')
		for i in range(3):
			for j in range(3):
				conf = 100 * self.confusion[i][j]/num_of_y[i]
				print(conf, end=' ')
			print()
		pickle.dump(self,open('DeepPong.txt','wb'))


				#Training done
				# np.random.shuffle(self.data)
				# correct = 0
				# for i in range(N):
				# 	A = self.data[i][:5]
				# 	y = self.data[i][5]
				# 	classification = self.FourLayerNetwork(A, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, 1,n)
				# 	if(classification == y):
				# 		correct += 1

				# accuracy = 100 *  correct / N
				# print()
				# print('Accuracy: ', accuracy, '%')




	def PrintAccuracyPlot(self):
		accuracy = np.array(self.accuracy_plot)
		accuracy = np.divide(accuracy,100)
		plt.plot(self.epoch_plot,accuracy)
		plt.plot(self.epoch_plot, self.loss_plot)
		plt.show()


	def play(self):
		score = 0
		R = 0
		while(R != -1):
			n = 0
			state = self.mdp.get_state()
			state_norm = np.zeros(5)
			for i in range(5):
				state_norm[i] = (state[i] - self.stats[i][0])/self.stats[i][1]
			y = []
			# print(state)
			action = self.FourLayerNetwork(state_norm, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, 1,n)

			R = self.mdp.update_environment(action)

			if(R > 0):
				score += R
			# print(score)

		return score


	def play_x(self,num_games):
		total = 0
		for i in range(num_games):	
			s = self.play()
			# if(s>0):
				# print('game: ',i, 'score: ', s)
			total += s
			self.mdp.init_envvironment()

		average = total/num_games
		print('Average hits per game: ', average)
	

DP = pickle.load(open('DeepPong.txt','rb'))
DP.mdp = MDP()
# DP = DeepPong()
# DP.MiniBatchGD(1000)
# DP.PrintAccuracyPlot()
DP.play_x(200)
