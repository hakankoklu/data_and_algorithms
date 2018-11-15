"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import deque


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        wg = WordGraph(wordList)
        return wg.get_paths(beginWord, endWord)


class WordGraph:

    def __init__(self, word_list):
        self.words = set(word_list)
        self.word_graph = {}
        self.build_graph()

    def build_graph(self):
        for word in self.words:
            self.word_graph[word] = self.get_word_neighbors(word)

    def get_word_neighbors(self, word):
        neighbors = set()
        abc = 'qwertyuiopasdfghjklzxcvbnm'
        for ind in range(len(word)):
            for let in abc:
                candidate = word[:ind] + let + word[ind + 1:]
                if candidate in self.words and candidate != word:
                    neighbors.add(candidate)
        return neighbors

    def make_directed_graph(self, start, end):
        parent_tree = {start: ({start}, 0)}
        to_visit = deque([start])
        while len(to_visit) > 0:
            current = to_visit.pop()
            distance = parent_tree[current][1] + 1
            neighbors = self.word_graph[current]
            for neighbor in neighbors:
                if neighbor not in parent_tree:
                    parent_tree[neighbor] = ({current}, distance)
                    to_visit.appendleft(neighbor)
                elif parent_tree[neighbor][1] == distance:
                    parent_tree[neighbor][0].add(current)
                    to_visit.appendleft(neighbor)
        return parent_tree

    def get_paths(self, start, end):
        if end not in self.words:
            return []
        paths = []
        path = []
        visited = {}
        directed_graph = self.make_directed_graph(start, end)
        if end not in directed_graph:
            return []
        self._get_paths(end, start, paths, path, visited, directed_graph)
        for path in paths:
            path.reverse()
        return paths

    def _get_paths(self, u, v, paths, path, visited, graph):
        visited[u] = True
        path.append(u)
        if u == v:
            paths.append(path[:])
        else:
            for i in graph[u][0]:
                if not visited.get(i):
                    self._get_paths(i, v, paths, path, visited, graph)
        path.pop()
        visited[u] = False


if __name__ == '__main__':
    words = ["hot","dog"]
    s = Solution()
    print(s.findLadders('hot', 'dog', words))