# Liste concatenate senza euristiche (list_naive)

class Node:
    def __init__(self, value):
        self.value = value
        self.representative = self
        self.next = None

class DisjointSetListNaive:
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
            return  # Già nello stesso insieme

        # Collega la lista di y alla fine di quella di x
        node = rep_x
        while node.next:
            node = node.next
        node.next = rep_y

        # Aggiorna i rappresentanti nella lista di y
        node = rep_y
        while node:
            node.representative = rep_x
            node = node.next

if __name__ == "__main__":
    # Esempio di utilizzo
    ds = DisjointSetListNaive()
    for i in range(1, 6):
        ds.make_set(i)

    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(2, 3)

    for i in range(1, 6):
        print(f"Elemento {i} -> Insieme rappresentato da {ds.find_set(i)}")
