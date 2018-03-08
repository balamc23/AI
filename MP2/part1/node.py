

class Node:
	def __init__(self):
		self.widgets = [['a','e','d','c','a'],
				   ['b','e','a','c','d'],
				   ['b','a','b','c','e'],
				   ['d','a','d','b','d'],
				   ['b','e','c','b','d']]
		# creating list of all remaining nodes		   
		self.remaining = [self.widgets[i//5][i%5] for i in range(25)] 	  
		# all possible moves
		self.possibilities = set([self.widgets[i][0] for i in range(5)])
		self.current_path = []
		self.current_cost = 0
		self.prev = 0
		self.current_cost1 = 0
	def __lt__(self,other):
		if len(self.current_path) > len(other.current_path):
			return 0
		else:
			return 1	



a = Node()
# print(a.possibilities)		