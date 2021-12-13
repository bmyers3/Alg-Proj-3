##Algorithms Project 3 Question 2
##Group: Braeden Myers, Josh Barber, Ian McGiness

import networkx as nx
import networkx.drawing

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

G.add_edge(1,3)
G.add_edge(4,12)
G.add_edge(3,2)
G.add_edge(3,5)
G.add_edge(2,1)
G.add_edge(4,1)
G.add_edge(4,2)
G.add_edge(7,10)
G.add_edge(5,6)
G.add_edge(5,8)
G.add_edge(6,7)
G.add_edge(6,8)
G.add_edge(10,9)
G.add_edge(8,9)
G.add_edge(8,10)
G.add_edge(9,5)
G.add_edge(9,11)
G.add_edge(10,11)
G.add_edge(11,12)

options = {'node_color': 'yellow', 'node_size': 250, 'width': 0.5, 'with_labels': True}

nx.draw_spring(G, **options)

C = nx.DiGraph(G)
D = list(nx.strongly_connected_components(G))
