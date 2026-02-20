import matplotlib.pyplot as plt
import networkx as nx


#А*, Б, В*, Г, Д, Е, Ж, 3, И* --> A*, B, C*, D, E, F, G, H, I*

G = nx.DiGraph()
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("B", "C"), ("B", "F"), ("C", "F"), ("C", "G"), ("D", "C"), ("D", "G"), ("E", "D"), ("E", "G"), ("E", "H"), ("F", "G"), ("F", "I"), ("G", "I"), ("H", "G"), ("H", "I")]
G.add_edges_from(edges)

plt.figure(figsize=(5, 5))
nx.draw(G,  with_labels=True, node_color='lightgreen', edge_color='black', width=3, arrows=True)
plt.show()



def find_path(edges, start_node, end_node, visited = []):
    if start_node in visited:
        return

    elif start_node == end_node:
        print(f"Path successful!")
        global path_counter
        path_counter += 1
        return

    else:
        for i in edges:
            if i[0] == start_node:
                find_path(edges, i[1], end_node, visited + [start_node])

path_counter = 0
find_path(edges, "A", "C")
a_c = path_counter
print(f"There are {a_c} ways to get from 'A' to 'C'.")

path_counter = 0
find_path(edges, "C", "I")
c_i = path_counter
print(f"There are {c_i} ways to get from 'C' to 'I'.")


print(f"Eventually, there are {a_c * c_i} ways to get from 'A' to 'I', having have visited C.")