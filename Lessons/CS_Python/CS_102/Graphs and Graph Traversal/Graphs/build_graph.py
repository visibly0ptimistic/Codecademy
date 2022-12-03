class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex):
        self.edges[vertex] = True

    def get_edges(self):
        return list(self.edges.keys())

class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from {0} to {1}".format(from_vertex.value, to_vertex.value))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value)

#Make the Graph instance here
railway = Graph()

#Make the Vertex instance here
station_one = Vertex("Ballahoo")
station_two = Vertex("Penn")

#Call .add_vertex() here
railway.add_vertex(station_one)
railway.add_vertex(station_two)

#Call .add_edge() here
railway.add_edge(station_one, station_two)
print("Edges for {0}: {1}".format(station_one.value, station_one.get_edges()))
print("Edges for {0}: {1}".format(station_two.value, station_two.get_edges()))