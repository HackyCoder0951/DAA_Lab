class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def find_parent(parents, vertex):
    return parents[vertex]

def union(parents, u, v):
    old_parent = parents[v]
    new_parent = parents[u]
    for i in range(len(parents)):
        if parents[i] == old_parent:
            parents[i] = new_parent

def kruskal_algorithm(edges, n):
    # Sort edges by weight
    edges.sort(key=lambda edge: edge.w)
    parents = [i for i in range(n)]
    mst = []
    total_cost = 0

    for edge in edges:
        u_rep = find_parent(parents, edge.u)
        v_rep = find_parent(parents, edge.v)
        if u_rep != v_rep:
            mst.append(edge)
            total_cost += edge.w
            union(parents, edge.u, edge.v)

    print("\nMinimum Spanning Tree (MST) Edges and Weights:")
    for edge in mst:
        print(f"{edge.u} - {edge.v} \tWeight: {edge.w}")
    print(f"Total cost of MST: {total_cost}")

def take_input():
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (use 0 for no connection):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print("Error: Row length must match number of vertices.")
            return
        graph.append(row)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicate edges (undirected)
            if graph[i][j] != 0:
                edges.append(Edge(i, j, graph[i][j]))

    kruskal_algorithm(edges, n)

# Run
take_input()
