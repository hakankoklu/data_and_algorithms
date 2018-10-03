"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
from collections import defaultdict
import heapq


class Graph:

    def __init__(self):
        self.edges = defaultdict(dict)
        self.vertices = set()

    def add_edge(self, v1, v2, weight):
        self.vertices = self.vertices.union(([v1, v2]))
        self.edges[v1][v2] = weight


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        g = Graph()
        for u, v, cost in flights:
            g.add_edge(u, v, cost)
        distance_map = {(0, src): 0}  # (edges, node): distance
        pq = []
        heapq.heappush(pq, (0, 0, src))  # (distance, edges, node)
        while pq:
            distance, stops, node = heapq.heappop(pq)
            if distance_map.get((stops, node), float("inf")) < distance:
                continue
            if stops > K + 1:
                continue
            if node == dst:
                return distance
            for neighbor, weight in g.edges[node].items():
                if node in g.edges[neighbor] and distance_map.get((stops - 1, neighbor), float("inf")) < distance + weight:
                    continue
                if distance_map.get((stops + 1, neighbor), float("inf")) > distance + weight:
                    distance_map[(stops + 1, neighbor)] = distance + weight
                    heapq.heappush(pq, (distance + weight, stops + 1, neighbor))
        return -1


if __name__ == '__main__':
    n = 4
    edges = [[0, 1, 100], [1, 0, 100], [1, 2, 100], [0, 2, 500], [2, 3, 100]]
    src = 0
    dst = 3
    k = 1
    s = Solution()
    print(s.findCheapestPrice(n, edges, src, dst, k))
