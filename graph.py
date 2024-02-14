from node import Node
start_node = '__start__'
end_node = '__end__'
class Graph:
    def __init__(self):
        self.nodes = {start_node: Node(start_node), end_node: Node(end_node)}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_node, to_node):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.nodes[from_node].add_neighbor(to_node)

    def get_nodes(self):
        return self.nodes.keys()

    def find_best_paths(self, n=1):
        # Priority queue to store the best N paths found so far
        best_paths = []

        # Stack to maintain the current paths being explored
        stack = [([(start_node, 0)], 0)]  # Initial path with start node and weight 0

        # Iteratively explore paths until the stack is empty
        while stack:
            current_path, current_weight = stack.pop()

            # Get the last node in the current path
            current_node, _ = current_path[-1]

            # If the last node is the end node, add the path to the priority queue
            if current_node == end_node:
                best_paths.append((current_path, current_weight))
                # Sort the best paths by weight and keep only the top N paths
                best_paths.sort(key=lambda x: x[1], reverse=True)
                best_paths = best_paths[:n]
                continue

            # Explore neighbors of the current node
            for neighbor, weight in self.nodes[current_node].neighbors.items():
                # If the neighbor has not been visited yet, add it to the stack
                if neighbor not in [node for node, _ in current_path]:
                    new_path = current_path + [(neighbor, weight)]
                    new_weight = current_weight + weight
                    stack.append((new_path, new_weight))

        return best_paths

    def __str__(self):
        result = ""
        for node_value in self.nodes:
            node = self.nodes[node_value]
            neighbors = node.get_neighbors()
            for neighbor in neighbors:
                weight = node.neighbors[neighbor]
                result += f"{node_value} --({weight})--> {neighbor}\n"
        return result