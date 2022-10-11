from math import inf, sqrt
from heapq import heappop, heappush

class graph_vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)

delhi = graph_vertex("New Delhi", 28.6448, 77.216721)
jaipur = graph_vertex("Jaipur", 26.92207, 75.778885)
varanasi = graph_vertex("Varanasi", 25.321684, 82.987289)
mumbai = graph_vertex("Mumbai", 19.07283, 72.88261)
chennai = graph_vertex("Chennai", 13.067439, 80.237617)
hyderabad = graph_vertex("Hyderabad", 17.387140, 78.491684)
kolkata = graph_vertex("Kolkata", 22.572645, 88.363892)
bengaluru = graph_vertex("Bengaluru", 12.972442, 77.580643)

euclidean_graph = {
    delhi: set([(jaipur, 2.243918), (varanasi, 6.65902), (mumbai, 10.507479), (chennai, 15.867576), (hyderabad, 11.329626), (kolkata, 12.693718), (bengaluru, 15.676582)]),
    jaipur: set([(mumbai, 8.366539), (delhi, 2.243918)]),
    varanasi: set([(delhi, 6.65902), (mumbai, 11.88077)]),
    mumbai: set([(delhi, 10.507479), (jaipur, 8.366539), (varanasi, 11.88077), (hyderabad, 5.856898), (kolkata, 15.87195), (bengaluru, 7.699756)]),
    chennai: set([(delhi, 15.867576), (kolkata, 12.50541), (hyderabad, 4.659195), (bengaluru, 2.658671)]),
    hyderabad: set([(delhi, 11.329626), (mumbai, 5.856898), (chennai, 4.659195), (bengaluru, 4.507721), (kolkata, 11.151231)]),
    kolkata: set([(delhi, 12.693718), (mumbai, 15.87195), (chennai, 12.50541), (hyderabad, 11.151231), (bengaluru, 14.437532)]),
    bengaluru: set([(delhi, 15.676582), (mumbai, 7.699756), (chennai, 2.658671), (hyderabad, 4.507721), (kolkata, 14.437532)])
}

# Change heuristic() below:
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return sqrt(x_distance * x_distance + y_distance * y_distance)

def a_star(graph, start, target):
    print("Starting A* algorithm!")
    count = 0
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1
                print("\nAt " + vertices_to_explore[0][1].name)
    
    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
    
    return paths_and_distances[target][1]

# Call a_star() on euclidean_graph to find the best route
# from jaipur to bengaluru:
a_star(euclidean_graph, jaipur, bengaluru)