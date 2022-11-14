
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def DFS(self, node, visited):
        visited.add(node)

        print(node, end=' ')
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

    def dfs(self, root_node):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFS(root_node, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
