import matplotlib.pyplot as plt
import networkx as nx


#А*, Б, В*, Г, Д, Е, Ж, 3, И* --> A*, B, C*, D, E, F, G, H, I*

G = nx.DiGraph()
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("B", "C"), ("B", "F"), ("C", "F"), ("C", "G"), ("D", "C"), ("D", "G"), ("E", "D"), ("E", "G"), ("E", "H"), ("F", "G"), ("F", "I"), ("G", "I"), ("H", "G"), ("H", "I")]
G.add_edges_from(edges)

plt.figure(figsize=(5, 5))
nx.draw(G,  with_labels=True, node_color='lightgreen', edge_color='black', width=3, arrows=True)
plt.show()