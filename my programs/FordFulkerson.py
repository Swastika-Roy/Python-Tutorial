from collections import deque, defaultdict

# BFS to find an augmenting path
def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

# Ford-Fulkerson using BFS (Edmonds-Karp)
def ford_fulkerson(graph, source, sink):
    # Build the residual graph
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            residual_graph[u][v] = graph[u][v]

    parent = {}
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        # Find minimum residual capacity along the path filled by BFS
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update the capacities in the residual graph
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Example usage:
graph = {
    's': {'A': 7, 'D': 4},
    'A': {'B': 5, 'C
