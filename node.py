class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        if neighbor in self.neighbors:
            self.neighbors[neighbor] += 1
        else:
            self.neighbors[neighbor] = weight

    def get_neighbors(self):
        return self.neighbors.keys()