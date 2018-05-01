import numpy as np
import math

class MarkovDecisionProcess:
	def __init__(self):
		# 0 - stay, 1 - up, 2 - down 
		self.actions = [ -0.04, 0 ,0.04]
		self.ball_x = None
		self.ball_y = None
		self.velocity_x = None
		self.velocity_y = None
		self.paddle_y = None
		self.paddle_height = 0.2

		self.init_envvironment()

	def init_envvironment(self):
		self.ball_x = 0.5
		self.ball_y = 0.5
		self.velocity_x = 0.03
		self.velocity_y = 0.00
		self.paddle_y = 0.5 - (self.paddle_height/2)

	def update_environment(self, action):
		# print('some')
		R = 0

		U = np.random.uniform(-0.015, 0.015)
		V = np.random.uniform(-0.03, 0.03)

		point_0 = (self.ball_x,self.ball_y)

		self.ball_x += self.velocity_x
		self.ball_y += self.velocity_y

		point_1 = (self.ball_x,self.ball_y)

		slope = (point_1[1]-point_0[1])/(point_1[0]-point_0[0])

		y_in_line = slope*(1 -point_0[0]) +point_0[1]

		self.paddle_y += self.actions[action]
		
		if(self.paddle_y < 0):
			self.paddle_y = 0

		if(self.paddle_y > 0.8):
			self.paddle_y = 0.8


		if(self.ball_y < 0):
			self.ball_y = -self.ball_y
			self.velocity_y = -self.velocity_y
			# return	R
		if(self.ball_y > 1):
			self.ball_y = 2 - self.ball_y
			self.velocity_y = -self.velocity_y
			# return R
		if(self.ball_x < 0):
			self.ball_x = -self.ball_x
			self.velocity_x = -self.velocity_x	
			# return R
		if(self.ball_x > 1 and (y_in_line >= self.paddle_y and y_in_line <= self.paddle_y + self.paddle_height) ):
			R = 1
			self.ball_x = 2 *1 - self.ball_x
			if(abs(self.velocity_x + U) < 1):
				self.velocity_x = -self.velocity_x + U
			else:
				self.velocity_x = -self.velocity_x
			if(abs(self.velocity_y + V) <1):
				self.velocity_y = self.velocity_y + V
			return R
		if(self.ball_x > 1 and (self.ball_y <= self.paddle_y or self.ball_y >= self.paddle_y + self.paddle_height)):
			R = -1
			# return R
		
		return R


	def get_state(self):
		return (self.ball_x, self.ball_y, self.velocity_x,self.velocity_y,self.paddle_y)





