class Vertex():

    def __init__(self, key):
        self.key = key
        self.connections = []

    def add_connections(self, n_list):
        self.neighbours.extend(n_list)

    def get_key(self):
        return self.key

    def get_connections(self):
        return self.connections

class Graph():

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def add_edge(self, key1, key2):
        if key1 not in self.vertices:
            nv1 = self.add_vertex(key1)
        if key2 not in self.vertices:
            nv2 = self.add_vertex(key2)
        nv1.add_connections([nv2])

kid_list = [7, 8, 10, 10, 9, 2, 9, 6, 3, 3]
bff_graph = Graph()
for kid, bff in enumerate(kid_list):
    bff_graph.add_edge(kid+1, bff)
