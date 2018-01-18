import random
import uuid

class Node:

	def __init__(self, key, data=None):
		self.key = key
		self.data = data
		self.edges = {}

	def __repr__(self):
		return 'Node#' + str(self.key)

	def connect_towards(self, g, weight):
		if self.edges.get(g.key):
			return
		edge = Edge((self, g), weight, True)
		self.edges[g.key] = edge

	def connect_undirected(self, g, weight):
		if self.edges.get(g.key):
			return
		edge = Edge((self, g), weight)
		self.edges[g.key] = edge
		g.edges[self.key] = edge

	def break_connection(self, g):
		edge = self.edges.pop(g.key)
		if not edge.directed:
			g.edges.pop(self.key)


class Edge:

	def __init__(self, nodes, weight=1, directed=False):
		"""
		directed:False nodes[0] <--> nodes[1]
		directed True:1 nodes[0] --> nodes[1]
		"""
		self.weight = weight
		self.nodes = nodes
		self.directed = directed

	def __repr__(self):
		direction = '->' if self.directed else '<->'
		return '{}{}{}:{}'.format(str(self.nodes[0]),
			direction,
			str(self.nodes[1]),
			str(self.weight))


def get_node(data=None):
	key = uuid.uuid4()
	return Node(key, data)


def make_undirected_graph(weight_span, node_number, ave_edge):
	if node_number > 100 or node_number < 2:
		raise ValueError('2 - 100 nodes is supported')
	nodes = []
	for i in range(node_number):
		nodes.append(Node(i))
	for i in range(ave_edge * node_number // 2):
		pair = random.sample(nodes, 2)
		weight = random.randint(*weight_span)
		pair[0].connect_undirected(pair[1], weight)

	return nodes