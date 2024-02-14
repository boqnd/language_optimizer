from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_node, to_node, weight=0):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.nodes[from_node].add_neighbor(to_node, weight)

    def get_nodes(self):
        return self.nodes.keys()

    def __str__(self):
        result = ""
        for node_value in self.nodes:
            node = self.nodes[node_value]
            neighbors = node.get_neighbors()
            for neighbor in neighbors:
                weight = node.neighbors[neighbor]
                result += f"{node_value} --({weight})--> {neighbor}\n"
        return result