from maze_loader import MazeLoader
import heapq
import queue
import time
import math

class GreedyMazeSolver:
	
	def __init__(self,maze):
		self.maze = maze

	def find_greedy_bfs(self):
		#initializes all local variables needed
		start = self.maze.start
		end = self.maze.end
		#set to check for already visited cells
		visitited = set()
		#solution dict
		draw_solution = {start:start}
		solution = []
		solution_set = set()
		# Add start to queue
		ts = time.time()
		#q = queue.Queue()
		d = self.get_manhattan(start,end)
		q = [(d, start)]
		visitited = set()
		maze_done  = 0
		nodes = 0
		
		while(len(q) != 0):
			curr_node= heapq.heappop(q)
			curr_pos = curr_node[1]
			nodes +=1
			neighbors = self.get_neighbors(curr_pos)
			for pos in neighbors:
				x, y = pos[0], pos[1]
				if(self.maze.maze_array[x][y] != '%'):
					if(pos not in visitited):
						d = self.get_manhattan(pos,end)
						heapq.heappush(q,(d,pos))
						#add pos to visited set
						draw_solution[pos] =curr_pos
						visitited.add(pos)
				if(self.maze.maze_array[x][y] == "."):
					print("found solution")
					ts2 = time.time()
					draw_solution[pos] =curr_pos
					maze_done =1
					break
			if(maze_done):
				break
						

		# Set end as top node
		solution.append(draw_solution[end])
		#loop to add parent node
		i =1
		while solution[i-1] != self.maze.start:
			dict_index = solution[i-1]
			solution.append(draw_solution[dict_index])
			solution_set.add(solution[i])
			i+=1 	

		
		point = end
		while(point != self.maze.start):
			point = draw_solution[point]
			self.maze.maze_array[point[0]][point[1]] = '.'
		self.maze.maze_array[start[0]][start[1]] = "P"

		for item in self.maze.maze_array:
			for c in item:	
				print(c, end = ' ')
			print()

		print(nodes, "nodes expanded")
		print(len(solution), "steps in path")
		print((ts2-ts), "Seconds")
		print()

	def get_neighbors(self, cell):
		x, y = cell[0], cell[1]
		return [
			(x + 1, y),
			(x - 1, y),
			(x, y + 1),
			(x, y - 1),
		]

	def get_manhattan(self, pos,end):
		x, y = pos[0], pos[1]
		x2, y2 = end[0], end[1]
		return abs(x2-x) + abs(y2-y)


m = MazeLoader(MazeLoader.medium)
greedy = GreedyMazeSolver(m)
greedy.find_greedy_bfs()

m2 = MazeLoader(MazeLoader.big)
greedy2 = GreedyMazeSolver(m2)
greedy2.find_greedy_bfs()

m3 = MazeLoader(MazeLoader.last)
greedy3 = GreedyMazeSolver(m3)
greedy3.find_greedy_bfs()

