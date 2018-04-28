import numpy as np 
import math
from mdp_env import MarkovDecisionProcess as MDP
from progress import printProgressBar
from time import sleep


Num_States = 10369	# 12*12*3*2*12 +1<---  how to get num states
alpha = 0.2
gamma = 0.2


class SARSA:

	def  __init__(self):
		self.Qtable = {}
		self.mdp = MDP()
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
					x_next = self.Qtable[new_state][action]
				self.Qtable[state][action] = x + alpha* (R + gamma*x_next - x)

			score += R

		return score


	def train(self):
		Iterations = 50000
		printProgressBar(0, Iterations, prefix = 'Training:', suffix = 'Complete', length = 50)
		for i in range(Iterations):
			# print('iteration: ',i)
			s = self.play(1)
			self.mdp.init_envvironment()
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


S = SARSA()
S.train()
S.test()





