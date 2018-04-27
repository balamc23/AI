import numpy as np 
import math
from mdp_env import MarkovDecisionProcess as MDP

Num_States = 10369	# 12*12*3*2*12 +1<---  how to get num states


class QLearn:

	def  __init__(self):
		self.Qtable = {}
		for x_pos in range(12):
			for y_pos in range(12):
				for x_vel in range(2):
					for y_vel in range(3):
						for paddle_y in range(12):
							self.Qtable[(x_pos,y_pos,x_vel,y_vel,paddle_y)] = [0,0,0]

		


