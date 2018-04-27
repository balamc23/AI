import numpy as np
import math

class MarkovDecisionProcess:
	def __init__(self):
		# 0 - stay, 1 - up, 2 - down 
		self.actions = [0, 0.04, -0.04]
		self.ball_x = None
		self.ball_y = None
		self.velocity_x = None
		self.velocity_y = None
		self.paddle_y = None
		self.paddle_height = 0.2

		self.board_actions = [0, 0.04, -0.04]
		self.board_ball_x = None
		self.board_ball_y = None
		self.board_velocity_x = None
		self.board_velocity_y = None
		self.board_paddle_y = None
		self.board_paddle_height = math.floor(self.paddle_height * 12)

		self.init_envvironment()
		self.init_board()

	def init_envvironment(self):
		self.ball_x = 0.5
		self.ball_y = 0.5
		self.velocity_x = 0.03
		self.velocity_y = 0.01
		self.paddle_y = 0.5 - (self.paddle_height/2)

	def update_environment(self, action):
		U = np.random.uniform(-0.015, 0.015)
		V = np.random.uniform(-0.03, 0.03)
		self.ball_x += self.velocity_x
		self.ball_y += self.velocity_y

		if(self.ball_y < 0):
			self.ball_y = -self.ball_y
			self.velocity_y = -self.velocity_y	
		if(self.ball_y > 1):
			self.ball_y = 2 - self.ball_y
			self.velocity_y = -self.velocity_y
		if(self.ball_x < 0):
			self.ball_x = -self.ball_x
			self.velocity_x = -self.velocity_x	
		if(self.ball_x == 1 and (self.ball_y >= self.paddle_y and self.ball_y <= self.paddle_y + self.paddle_height)):
			self.ball_x = 2 *1 - self.ball_x
			if(abs(self.velocity_x + U) < 1):
				self.velocity_x = -self.velocity_x + U
			if(abs(self.velocity_y + V) <1):
				self.velocity_y = self.velocity_y + V

		# updating position of ball
#		self.ball_x += self.velocity_x
#		self.ball_y += self.velocity_y

	def init_board(self):
		self.board_ball_x = 6
		self.board_ball_y = 6
		self.board_velocity_x = 1
		self.board_velocity_y = 0			
		self.board_paddle_y = math.floor(12 * self.paddle_y/(1-self.paddle_height))
		if(self.paddle_y == (1 - self.paddle_height)):
			self.board_paddle_y = 11

	def update_board(self):
		# updating position of ball
		self.ball_x += self.velocity_x
		self.ball_y += self.velocity_y

		if(self.board_ball_y < 0)board_:
			self.board_ball_y = -self.board_ball_y
			self.board_velocity_y = -self.board_velocity_y	
		if(self.board_ball_y > 1):
			self.board_ball_y = 2 - self.board_ball_y
			self.board_velocity_y = -self.board_velocity_y
		if(self.board_ball_x < 0):
			self.board_ball_x = -self.board_ball_x
			self.board_velocity_x = -self.board_velocity_x	
		if(self.board_ball_x == 1 and (self.board_ball_y >= self.board_paddle_y and self.board_ball_y <= self.board_paddle_y + self.board_paddle_height)):
			self.board_ball_x = 2 *12 - self.board_ball_x
			self.board_velocity_x = -self.board_velocity_x
			if(abs(self.velocity_y ) < 0.015):
				self.board_velocity_y = 0

		# # updating position of ball
		# self.ball_x += self.velocity_x
		# self.ball_y += self.velocity_y


