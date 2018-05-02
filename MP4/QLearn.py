import numpy as np 
import math
from mdp_env import MarkovDecisionProcess as MDP
from mdp_env_ec import MarkovDecisionProcess_EC as MDP_EC
from progress import printProgressBar
from time import sleep
import copy
import random
import matplotlib.pyplot as plt
import pickle

Num_States = 10369	# 12*12*3*2*12 +1<---  how to get num states
# alpha = 0.2
gamma = 0.2
C = 5

 # α(N)=C/(C+N(s,a))

class QLearn:

	def  __init__(self):
		self.Qtable = {}
		self.N = {}
		self.N_ec = {}
		self.Qtable_ec = {}
		self.mdp = MDP()
		self.mdp_ec = MDP_EC()
		self.epoch_plot = []
		self.avg_plot = []
		self.epoch_plot_ec = []
		self.avg_plot_ec = []
		for x_pos in range(12):
			for y_pos in range(12):
				for x_vel in (-1,1):
					for y_vel in (-1,0,1):
						for paddle_y in range(12):
							self.Qtable[(x_pos,y_pos,x_vel,y_vel,paddle_y)] = [0,0,0]
							self.N[(x_pos,y_pos,x_vel,y_vel,paddle_y)] = [0,0,0]
							self.N_ec[(x_pos,y_pos,x_vel,y_vel,paddle_y)] = [0,0,0]

	def play(self,train,num):
		score = 0
		R = 0
		while(R != -1):

			state = self.mdp.get_d_state()
			temp = np.array(self.Qtable[state])
			action = np.argmax(temp)
			if(train == 1 and num < 50000):
				action += random.choice((-1,0,1))
				action = action%3

			self.N[state][action] += 1

			R = self.mdp.update_environment(action)
			new_state = self.mdp.get_d_state()
			# print(R,state,new_state)
			if(train == 1):
				x = self.Qtable[state][action]
				N = self.N[state][action]
				alpha = C/(C +N)
				#misses paddle
				if(R < 0):
					return score
				#doesnt lose
				else:
					x_next = max(self.Qtable[new_state])

				self.Qtable[state][action] = x + alpha* (R + gamma*x_next - x)

			score += R

		return score

	def play_ec(self,train,num):
		score = 0
		R = 0
		while(R != -1):

			state = self.mdp_ec.get_d_state()
			temp = np.array(self.Qtable_ec[state])
			action = np.argmax(temp)
			if(train == 1 and num < 50000):
				action += random.choice((-1,0,1))
				action = action%3

			self.N_ec[state][action] += 1

			R = self.mdp_ec.update_environment(action)
			new_state = self.mdp_ec.get_d_state()
			# print(R,state,new_state)
			if(train == 1):
				x = self.Qtable_ec[state][action]
				N = self.N_ec[state][action]
				alpha = C/(C +N)
				#misses paddle
				if(R < 0):
					return score
				#doesnt lose
				else:
					x_next = max(self.Qtable_ec[new_state])

				self.Qtable_ec[state][action] = x + alpha* (R + gamma*x_next - x)

			score += R

		return score

	def train(self):
		Iterations = 100000
		printProgressBar(0, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
		for i in range(Iterations):
			s = self.play(1,i)
			self.mdp.init_envvironment()
			printProgressBar(i + 1, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
			if(i%1000 == 0 or i == Iterations-1):
				num_success = 0
				total = 0
				for j in range(200):
					s = self.play(0,i)
					total += s		
					self.mdp.init_envvironment()
				average = total/200
				# print('Average Score: ', average)
				self.epoch_plot.append(i)
				self.avg_plot.append(average)

		pickle.dump(self,open('Qtable.txt','wb'))

	def train_ec(self):
		self.Qtable_ec = copy.deepcopy(self.Qtable)
		Iterations = 100000
		printProgressBar(0, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
		for i in range(Iterations):
			s = self.play_ec(1,i)
			self.mdp_ec.init_envvironment()
			printProgressBar(i + 1, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
			if(i%1000 == 0 or i == Iterations-1):
				num_success = 0
				total = 0
				for j in range(200):
					s = self.play_ec(0,i)
					total += s		
					self.mdp_ec.init_envvironment()
				average = total/200
				# print('Average Score: ', average)
				self.epoch_plot_ec.append(i)
				self.avg_plot_ec.append(average)
		pickle.dump(self,open('Qtable.txt','wb'))

	def test(self):
		num_success = 0
		total = 0
		for i in range(200):
			s = self.play(0,i)
			total += s		
			if (s >= 9):
				print('game', i, 'score: ' , s)
				num_success += 1
			self.mdp.init_envvironment()

		average = total/200
		print('Average Score: ', average)
		print('number of successful games: ', num_success)
		


	def test_ec(self):
		num_success = 0
		total = 0
		for i in range(200):
			s = self.play_ec(0,i)
			total += s
			if (s >= 9):
				print('game', i, 'score: ' , s)
				num_success += 1
			self.mdp_ec.init_envvironment()

		average = total/200
		print('Average Score: ', average)
		print('number of successful games: ', num_success)


	def PrintPlot(self):
		plt.plot(self.epoch_plot, self.avg_plot)
		plt.title('Mean episode rewards vs episodes 1.1')
		plt.show()

	def PrintPlot_ec(self):
		plt.plot(self.epoch_plot_ec, self.avg_plot_ec)
		plt.title('Mean episode rewards vs episodes 1.2')
		plt.show()

	
# Q = pickle.load(open('Qtable.txt','rb'))
Q = QLearn()
Q.train()
Q.PrintPlot()
Q.test()

Q.train_ec()
Q.PrintPlot_ec()
Q.test_ec()





