import networkx as nx
import matplotlib.pyplot as plt

def building_graph(G):
	G.add_node('a')
	G.add_node('b')
	G.add_node('c')
	G.add_node('d')
	G.add_node('e')

	G.add_edge('a', 'b', weight = 1064)
	G.add_edge('a', 'c', weight = 673)
	G.add_edge('a', 'd', weight = 1401)
	G.add_edge('a', 'e', weight = 277)

	G.add_edge('b', 'a', weight = 1064)
	G.add_edge('b', 'c', weight = 958)
	G.add_edge('b', 'd', weight = 1934)
	G.add_edge('b', 'e', weight = 337)

	G.add_edge('c', 'a', weight = 673)
	G.add_edge('c', 'b', weight = 958)
	G.add_edge('c', 'd', weight = 1001)
	G.add_edge('c', 'e', weight = 399)

	G.add_edge('d', 'a', weight = 1401)
	G.add_edge('d', 'b', weight = 1934)
	G.add_edge('d', 'c', weight = 1001)
	G.add_edge('d', 'e', weight = 387)

	G.add_edge('e', 'a', weight = 277)
	G.add_edge('e', 'b', weight = 337)
	G.add_edge('e', 'c', weight = 399)
	G.add_edge('e', 'd', weight = 387)

	# Atlanta, Boston, Chicago, Denver, and Edmonton
	labels = {'a': 'Atlanta',  'b': 'Boston', 'c': 'Chicago', 'd': 'Denver', 'e': 'Edmonton'}
	H = nx.relabel_nodes(G, labels)
	return H

	# print('G')
	# print(G.nodes())
	# print(G.edges())

	# print('H')
	# print(H.nodes())
	# print(H.edges())

	# nx.draw(H, with_labels = True)
	# plt.savefig('plot.png')
	# plt.show()

def main():
	graph = nx.Graph()
	h_graph = building_graph(graph)
	nx.draw(h_graph, with_labels = True)
	plt.savefig('plot')
	plt.show()


if __name__ == "__main__":
	main()








