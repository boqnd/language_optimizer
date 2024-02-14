class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor):
        if neighbor in self.neighbors:
            self.neighbors[neighbor] += 1
        else:
            self.neighbors[neighbor] = 1

    def get_neighbors(self):
        return self.neighbors.keys()