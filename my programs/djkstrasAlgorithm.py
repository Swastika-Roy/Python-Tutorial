import heapq


def dijkstra(graph, start):
    # Initialize distances with infinity and set start node distance to 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes to visit, starting with the start node
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've already found a better path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"To {node}: {distance}")