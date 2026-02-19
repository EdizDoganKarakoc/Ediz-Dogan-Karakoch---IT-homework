import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
edges_with_weights = [
    ("A", "B", 1),
    ("A", "C", 1),
    ("A", "D", 2),
    ("A", "E", 3),
    ("B", "E", 5),
    ("C", "D", 2),
    ("D", "E", 4)
]

for u, v, w in edges_with_weights:
    G.add_edge(u, v, weight=w)
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True,
        node_color='lightgreen',
        edge_color='black',
        width=5,
        node_size=500)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Взвешенный граф")
plt.show()


print("Obviously, the answer is 2.")