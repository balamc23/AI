import numpy as np 
import math
from mdp_env import MarkovDecisionProcess as MDP
from mdp_env_ec import MarkovDecisionProcess_EC as MDP_EC
from progress import printProgressBar
from time import sleep
import copy


Num_States = 10369	# 12*12*3*2*12 +1<---  how to get num states
alpha = 0.2
gamma = 0.2


class QLearn:

	def  __init__(self):
		self.Qtable = {}
		self.Qtable_ec = {}
		self.mdp = MDP()
		self.mdp_ec = MDP_EC()
		for x_pos in range(12):
			for y_pos in range(12):
				for x_vel in (-1,1):
					for y_vel in (-1,0,1):
						for paddle_y in range(12):
							self.Qtable[(x_pos,y_pos,x_vel,y_vel,paddle_y)] = [0,0,0]

	def play(self,train):
		score = 0
		R = 0
		while(R != -1):

			state = self.mdp.get_d_state()

			action = self.Qtable[state].index(max(self.Qtable[state]))

			R = self.mdp.update_environment(action)

			new_state = self.mdp.get_d_state()

			if(train == 1):
				x = self.Qtable[state][action]
				#misses paddle
				if(R < 0):
					x_next = 0			# note sure if setting this to 0 is the right move
				#doesnt lose
				else:
					x_next = max(self.Qtable[new_state])
				self.Qtable[state][action] = x + alpha* (R + gamma*x_next - x)

			score += R

		return score

	def play_ec(self,train):
		score = 0
		R = 0
		while(R != -1):

			state = self.mdp_ec.get_d_state()

			action = self.Qtable_ec[state].index(max(self.Qtable_ec[state]))

			R = self.mdp_ec.update_environment(action)

			new_state = self.mdp_ec.get_d_state()

			if(train == 1):
				x = self.Qtable_ec[state][action]
				#misses paddle
				if(R < 0):
					x_next = 0			# note sure if setting this to 0 is the right move
				#doesnt lose
				else:
					x_next = max(self.Qtable_ec[new_state])
				self.Qtable_ec[state][action] = x + alpha* (R + gamma*x_next - x)

			score += R

		return score

	def train(self):
		Iterations = 50000
		printProgressBar(0, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
		for i in range(Iterations):
			s = self.play(1)
			self.mdp.init_envvironment()
			printProgressBar(i + 1, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)

	def train_ec(self):
		self.Qtable_ec = copy.deepcopy(self.Qtable)
		Iterations = 50000
		printProgressBar(0, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
		for i in range(Iterations):
			s = self.play_ec(1)
			self.mdp_ec.init_envvironment()
			printProgressBar(i + 1, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)

	def test(self):
		num_success = 0
		for i in range(200):
			s = self.play(0)
			if (s >= 9):
				print('game', i, 'score: ' , s)
				num_success += 1
			self.mdp.init_envvironment()

		print('number of successful games: ', num_success)

	def test_ec(self):
		num_success = 0
		for i in range(200):
			s = self.play_ec(0)
			if (s >= 9):
				print('game', i, 'score: ' , s)
				num_success += 1
			self.mdp_ec.init_envvironment()

		print('number of successful games: ', num_success)

	

Q = QLearn()
Q.train()
Q.test()
Q.train_ec()
Q.test_ec()





