class MinHeap:
    def __init__(self):
        self._heap = []
        self._heap.append(0)

    def getParent(self, i): return self._heap[i//2]
    def getLeft(self, i): return self._heap[i*2]
    def getRight(self, i): return self._heap[i*2 + 1]
    def getSize(self): return len(self._heap) - 1
    def isEmpty(self): return self.getSize() == 0
    def __str__(self): return str(self._heap)
    def insert(self, n):
        self._heap.append(n)
        i = self.getSize()
        while i != 1 and n < self.getParent(i):
            self._heap[i] = self.getParent(i)
            i = i // 2
        self._heap[i] = n

    def delete(self):
        parent, child = 1, 2
        if not self.isEmpty():
            hroot = self._heap[1]
            last = self._heap[self.getSize()]
            while child <= self.getSize():
                if child < self.getSize() and self.getLeft(parent) > self.getRight(parent):
                    child += 1
                if last <= self._heap[child]:
                    break
                self._heap[parent] = self._heap[child]
                parent = child
                child *= 2

            self._heap[parent] = last
            self._heap.pop(-1)
            return hroot

    def printHeap(self):
        level = 1
        for i in range(1, self.getSize() + 1):
            if i == level:
                print('')
                level *= 2
            print(str(self._heap[i]), end = ' ')
        print("\n------------------------")
