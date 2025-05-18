# Liste concatenate con unione pesata
class Node:
    def __init__(self, value):
        self.value = value
        self.representative = self
        self.next = None
        self.size = 1

class DisjointSetListWeighted:
    def __init__(self):
        self.members = {}  # value -> Node

    def make_set(self, x):
        node = Node(x)
        self.members[x] = node

    def find_set(self, x):
        return self.members[x].representative.value

    def union(self, x, y):
        rep_x = self.members[x].representative
        rep_y = self.members[y].representative

        if rep_x == rep_y:
            return

        # Scegli la lista più grande come destinazione
        if rep_x.size >= rep_y.size:
            larger, smaller = rep_x, rep_y
        else:
            larger, smaller = rep_y, rep_x

        # Trova la fine della lista più grande
        node = larger
        while node.next:
            node = node.next
        node.next = smaller

        # Aggiorna i rappresentanti e le taglie
        node = smaller
        while node:
            node.representative = larger
            node = node.next

        larger.size += smaller.size

if __name__ == "__main__":
    ds = DisjointSetListWeighted()
    for i in range(1, 6):
        ds.make_set(i)

    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(2, 3)

    for i in range(1, 6):
        print(f"Elemento {i} -> Insieme rappresentato da {ds.find_set(i)}")
