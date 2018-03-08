from graph import CityGraph
import matplotlib.pyplot as plt
from copy import deepcopy
from node import Node
import heapq

class ASTARSolver:
	def __init__(self):
		a = Node()
		self.loop=0
		self.first_iter = 1

		self.frontier = []

		self.frontier1 = []
		self.frontier2 = []
		self.frontier3 = []

		self.enum = {'a': 0, 
					 'b': 1,
					 'c': 2,
					 'd': 3,
					 'e': 4
					 }

		self.cost_array = [[0,1064,673,1401,277],
						   [1064,0,958, 1934, 337],
						   [673, 958, 0, 1001, 399],
						   [1401, 1934, 10001, 0, 387],
						   [277, 337, 399, 387, 0]]
		print("WTFFFFFF")
		init_pos = self.get_next_steps(a,0)
		print(init_pos)
		ret = [] #astar values pick smallest
		for i in init_pos:
			self.frontier = []
			print("the starting position is ",i[0], " \n")
			heapq.heappush(self.frontier,(0,i))
			ret.append(self.astar())
		for l in ret:
			print('path ', l[1][1].current_path)
			print('cost ', l[1][1].current_cost)
			print('stops ', len(l[1][1].current_path))



	def heuristic(self, a):
		return (a * 843.1)//6
	def heuristic2(self, a):
		return (a / 6)	

	def astar(self):
		
		# print("The popped element's remaining is  ",l[1][1].remaining, " the number is ", len(l[1][1].remaining) )
		while(1):
			l =	heapq.heappop(self.frontier)
			if (len(l[1][1].remaining) == 0):
				# print(" WHAT")
				print(" The cost is ",l[1][1].current_cost)
				return l
			print("The second arg is ",l)
			new_list= self.get_next_steps(l[1][1],l[1][0])
			print(" THE FUCKING LIST IS ",new_list)
			for i in new_list:
				# print("HERE I AM ")
				# print(len(new_list))
				
				# answer based on cost
				# heapq.heappush(self.frontier, (i[1].current_cost1, i))
				# answer based on stops
				heapq.heappush(self.frontier, (len(i[1].current_path) + self.heuristic2(len(i[1].remaining)), i))

	def get_next_steps(self, cur_node, prev_position):
		# print("At start of get next steps prev position is ", prev_position)
		# print("The frontier is \n", self.frontier)
		# print("remaining is ", len(cur_node.remaining))
		self.loop+=1
		# print("The loop var is ",self.loop)
		node_list = []
		# print(cur_node.possibilities)
		# cycling through possibilities
		for pos in cur_node.possibilities:
			# print("The possibility is ",pos)
			new_widgets = deepcopy(cur_node.widgets)
			new_remaining = []
			new_possibilities = set()
			new_current_path = deepcopy(cur_node.current_path)
			new_current_cost1 = deepcopy(cur_node.current_cost1)
			new_current_cost = deepcopy(cur_node.current_cost)
			# cycling through first elem and deleting what we have picked
			for i in range(len(cur_node.widgets)):
				if(len(new_widgets[i])!=0):	
					if cur_node.widgets[i][0] == pos:
						del new_widgets[i][0]
				new_remaining.extend(new_widgets[i])
				# print(new_remaining, len(new_remaining))
				# new first elem
				if(len(new_widgets[i])!=0):	
					new_possibilities.add(new_widgets[i][0])
			# print("The new widgets is ", new_widgets)
			new_current_path.append(pos)
			if(self.loop > 2):
				# print(self.first_iter, 'duh hello')
				print(prev_position)
				new_current_cost1 += self.cost_array[self.enum[prev_position]][self.enum[pos]] + self.heuristic(len(new_remaining))
				new_current_cost += self.cost_array[self.enum[prev_position]][self.enum[pos]]
			# print(" The position being appended is ", pos)
			node_list.append((pos, self.node_creator(new_widgets, new_remaining, new_possibilities, new_current_path, new_current_cost, prev_position, new_current_cost1)))
		if(self.first_iter):
			self.first_iter=0
		return node_list

	def node_creator(self, w, r, p, cp, cc, p1, cc1):	
		new_node = Node()
		new_node.widgets = deepcopy(w)
		new_node.remaining = deepcopy(r)
		new_node.possibilities = deepcopy(p)
		new_node.current_path = deepcopy(cp)
		new_node.current_cost = deepcopy(cc)
		new_node.prev = deepcopy(p1)
		new_node.current_cost1 = deepcopy(cc1)
		return new_node			

def main():
	astar = ASTARSolver()

if __name__ == "__main__":
	main()	
