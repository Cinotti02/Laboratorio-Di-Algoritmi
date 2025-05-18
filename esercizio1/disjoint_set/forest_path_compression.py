# Foresta con compressione del cammino (path compression)

class DisjointSetForest:
    def __init__(self):
        self.parent = {}  # elemento -> genitore

    def make_set(self, x):
        self.parent[x] = x

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            self.parent[root_y] = root_x

if __name__ == "__main__":
    # Esempio di utilizzo
    ds = DisjointSetForest()
    for i in range(1, 6):
        ds.make_set(i)

    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(2, 3)

    for i in range(1, 6):
        print(f"Elemento {i} -> Insieme rappresentato da {ds.find_set(i)}")
