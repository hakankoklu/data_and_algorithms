"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(dict)  # {'a': {'b': 2, 'c': 3}, 'b': {'c': 1.5}}

    def add_edge(self, u, v, weight):
        self.nodes.add(u)
        self.nodes.add(v)
        self.edges[u][v] = weight
        self.edges[v][u] = 1/weight

    def bfs_product(self, u, v):
        if not (u in self.nodes and v in self.nodes):
            return -1
        if u == v:
            return 1
        visited = set()
        to_visit = deque()
        to_visit.append(u)
        parent_map = {}
        found = False
        while to_visit:
            current = to_visit.popleft()
            visited.add(current)
            neighbors = self.edges[current]
            for neighbor, weight in neighbors.items():
                if neighbor == v:
                    found = True
                if neighbor not in visited:
                    parent_map[neighbor] = current
                    to_visit.append(neighbor)
            if found:
                break
        if not found:
            return -1
        parent = v
        product = 1
        while parent != u:
            current = parent
            parent = parent_map[parent]
            product *= self.edges[parent][current]
        return product


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = Graph()
        for equation, value in zip(equations, values):
            g.add_edge(equation[0], equation[1], value)
        result = []
        for u, v in queries:
            pr = g.bfs_product(u, v)
            result.append(pr)
        return result


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    s = Solution()
    print(s.calcEquation(equations, values, queries))
