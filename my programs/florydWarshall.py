import sys


def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.

    Args:
        graph: Adjacency matrix representation of the graph.
               graph[i][j] = weight from node i to node j.
               graph[i][i] = 0.
               If no edge exists, use infinity (float('inf')).

    Returns:
        dist: Matrix of shortest distances between all pairs.
        next_node: Matrix used to reconstruct shortest paths.
    """
    n = len(graph)

    # Initialize distance and next_node matrices
    dist = [[0] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
            if graph[i][j] != float('inf'):
                next_node[i][j] = j

    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Optional: Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Negative cycle detected!")
            return None, None

    return dist, next_node


def reconstruct_path(next_node, start, end):
    """
    Reconstruct shortest path from start to end using next_node matrix.

    Args:
        next_node: Next node matrix from floyd_warshall.
        start: Starting node index.
        end: Ending node index.

    Returns:
        List of nodes in the shortest path from start to end.
    """
    if next_node[start][end] is None:
        return []

    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)

    return path


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency matrix
    # Use float('inf') for no direct connection
    INF = float('inf')
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    dist, next_node = floyd_warshall(graph)

    if dist is not None:
        print("Shortest distances between all pairs:")
        for row in dist:
            print(row)

        print("\nExample paths:")
        for i in range(len(graph)):
            for j in range(len(graph)):
                path = reconstruct_path(next_node, i, j)
                print(f"Path from {i} to {j}: {path} (distance: {dist[i][j]})")