class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):  # No cycle
            ds.union(u, v)
            mst.append((u, v, w))
            total_cost += w

    print("\nMinimum Spanning Tree (MST):")
    for u, v, w in mst:
        print(f"{u} - {v} \tWeight: {w}")
    print(f"Total Cost of MST = {total_cost}")

# Example usage:
if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    kruskal(n, edges)
