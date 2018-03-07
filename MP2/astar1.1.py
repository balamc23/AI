import graph as gr
import matplotlib.pyplot as plt
import networkx as nx


# def astar():

def main():
	city_graph = gr.main()
	nx.draw(city_graph, with_labels = True)
	plt.savefig('plot')
	plt.show()

if __name__ == "__main__":
	main()	
