class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"( {str(self.data)} )"

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self, n):
        self.next = n

    def setData(self, d):
        self.data = d