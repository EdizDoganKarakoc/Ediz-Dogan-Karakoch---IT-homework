graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}




def optimal_path(graph, visited = []):
    if len(visited) == 0:
        print("visited")
        for key in graph:
            visited.append(key)
            optimal_path(graph, visited)



    elif len(set(visited)) != len(list(graph.items())):
        print("visited")
        unvisited_neighbors = []
        for neighbor in graph[visited[-1]]:
            if neighbor not in visited:
                unvisited_neighbors.append(neighbor)

        if len(unvisited_neighbors) == 0:
            for neighbor in graph[visited[-1]]:
                visited.append(neighbor)
                optimal_path(graph, visited)

        else:
            for neighbor in  graph[visited[-1]]:
                visited.append(neighbor)
                optimal_path(graph, visited)



    else:
        global path_counter
        if len(visited) < len(path_counter):
            path_counter = visited


path_counter = []

optimal_path(graph)
print(path_counter)