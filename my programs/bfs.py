from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph

    Args:
        graph (dict): Adjacency list representing the graph
        start: Starting node for BFS

    Returns:
        tuple: (visited nodes in order, parent dictionary)
    """
    visited = []  # List to keep track of visited nodes in order
    queue = deque()  # Initialize a queue
    parent = {start: None}  # To keep track of the parent of each node

    queue.append(start)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            # Explore neighbors
            for neighbor in graph[node]:
                if neighbor not in parent:  # If not visited yet
                    parent[neighbor] = node
                    queue.append(neighbor)

    return visited, parent


# Example usage
if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    visited_nodes, parent_dict = bfs(graph, start_node)

    print("BFS Visited Order:", visited_nodes)
    print("Parent Relationships:", parent_dict)

    # Optional: Print path from start node to a specific node
    target = 'F'
    path = []
    while target is not None:
        path.append(target)
        target = parent_dict.get(target)
    path.reverse()
    print(f"Path from {start_node} to F:", path)