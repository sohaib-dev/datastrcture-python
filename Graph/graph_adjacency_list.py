

class AdjacencyNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*self.vertices

    def add_edge(self, source, destination):
        node = AdjacencyNode(destination)
        node.next_node = self.graph[source]
        self.graph[source] = node

        node = AdjacencyNode(source)
        node.next_node = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.vertices):
            temp = self.graph[i]
            while temp:
                print(f'{temp.data} --> ', end='')
                temp = temp.next_node
            print("\n")

if __name__ == '__main__':
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
        



    print("\n")
