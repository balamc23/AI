from maze_loader import MazeLoader
import queue
import time

class BFSMazeSolver:

	def __init__(self, maze):
		self.maze = maze

	def find_BFS(self):
		#initializes all local variables needed
		start = self.maze.start
		#set to check for already visited cells
		visitited = set()
		#solution dict
		draw_solution = {start:start}
		solution = []
		solution_set = set()
		# Add start to queue
		ts = time.time()
		q = queue.Queue()
		visitited = set()
		maze_done  = 0
		q.put(start)
		steps = 0

		while(not q.empty()):
			#pop position off the queue
			curr_pos = q.get()
			steps +=1
			neighbors = BFSMazeSolver.get_neighbors(self,curr_pos)
			for pos in neighbors:
				x, y = pos[0], pos[1]
				if(self.maze.maze_array[x][y] != '%'):
					if(pos not in visitited):
						q.put(pos)
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
		solution.append(draw_solution[self.maze.end])

		#loop to add parent node
		i =1
		while solution[i-1] != self.maze.start:
			dict_index = solution[i-1]
			solution.append(draw_solution[dict_index])
			solution_set.add(solution[i])
			i+=1 	

		point = self.maze.end
		while(point != self.maze.start):
			point = draw_solution[point]
			self.maze.maze_array[point[0]][point[1]] = '.'
		self.maze.maze_array[start[0]][start[1]] = "P"

		for item in self.maze.maze_array:
			for c in item:	
				print(c, end = ' ')
			print()

		print(steps, "nodes expanded")
		print(len(solution), "steps in solution")
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


m = MazeLoader(MazeLoader.medium)
bfs = BFSMazeSolver(m)
bfs.find_BFS()

m2 = MazeLoader(MazeLoader.big)
bfs2 = BFSMazeSolver(m2)
bfs2.find_BFS()

m3 = MazeLoader(MazeLoader.last)
bfs3 = BFSMazeSolver(m3)
bfs3.find_BFS()

