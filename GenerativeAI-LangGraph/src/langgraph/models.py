class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


class LangGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, from_name, to_name, weight):
        if from_name not in self.nodes:
            self.add_node(from_name)
        if to_name not in self.nodes:
            self.add_node(to_name)
        self.nodes[from_name].add_edge(Edge(self.nodes[to_name], weight))