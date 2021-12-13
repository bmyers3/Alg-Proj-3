##Algorithms Project 3 Question 1
##Group: Braeden Myers, Josh Barber, Ian McGiness

import networkx as nx
import networkx.drawing

G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])

G.add_edge('A', 'B')
G.add_edge('A', 'E')
G.add_edge('A', 'F')
G.add_edge('B', 'C')
G.add_edge('B', 'F')
G.add_edge('C', 'D')
G.add_edge('C', 'G')
G.add_edge('D', 'G')
G.add_edge('E', 'F')
G.add_edge('E', 'I')
G.add_edge('G', 'J')
G.add_edge('I', 'J')
G.add_edge('I', 'M')
G.add_edge('M', 'N')

G.add_edge('H', 'K')
G.add_edge('H', 'L')
G.add_edge('K', 'L')
G.add_edge('K', 'O')
G.add_edge('L', 'P')

options = {'node_color': 'yellow', 'node_size': 250, 'width': 0.5, 'with_labels': True}

nx.draw_spring(G, **options)


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, G, 'A')


