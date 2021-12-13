##Algorithms Project 3 Question 2
##Group: Braeden Myers, Josh Barber, Ian McGiness

import networkx as nx
import networkx.drawing

G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

G.add_edge('A', 'B', weight = 22)
G.add_edge('A', 'C', weight = 9)
G.add_edge('A', 'D', weight = 12)
G.add_edge('B', 'C', weight = 35)
G.add_edge('B', 'F', weight = 36)
G.add_edge('B', 'H', weight = 34)
G.add_edge('C', 'D', weight = 4)
G.add_edge('C', 'E', weight = 65)
G.add_edge('C', 'F', weight = 42)
G.add_edge('D', 'I', weight = 30)
G.add_edge('D', 'E', weight = 33)
G.add_edge('E', 'F', weight = 18)
G.add_edge('E', 'G', weight = 23)
G.add_edge('F', 'G', weight = 39)
G.add_edge('F', 'H', weight = 24)
G.add_edge('G', 'H', weight = 25)
G.add_edge('G', 'I', weight = 21)
G.add_edge('I', 'H', weight = 19)

options = {'node_color': 'yellow', 'node_size': 250, 'width': 0.5, 'with_labels': True}

D = nx.dijkstra_path(G, 'A', 'G')

G2 = nx.minimum_spanning_tree(G)
nx.draw_circular(G2, **options)


