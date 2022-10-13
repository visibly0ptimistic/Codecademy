from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


# Define dijkstras() below:
def dijkstras(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = inf
    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

    return distances