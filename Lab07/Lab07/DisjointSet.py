# disjointSet
class DisjointSet:
    def __init__(self):
       self.parent = dict()
       self.rank = dict()

    def makeSet(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    def find(self, v):
        # !root
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def Union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1

            else:
                self.parent[root2] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] =+ 1