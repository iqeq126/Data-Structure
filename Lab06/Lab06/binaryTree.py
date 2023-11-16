from binaryNode import *
from queue import Queue
class binaryTree:
    def __init__(self, root=None):
        self.root = root

    def getRoot(self):
        return self.root
    def setRoot(self, node):
        self.root = node

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def printInorder(self, msg="In-order : "):
        print(msg, end = " ")
        self.inorder(self.getRoot())
        print()
    def inorder(self, n):
        if n is not None:
            self.inorder(n.getLeft())
            print(f"({n})", end="->")
            self.inorder(n.getRight())

    def printPreorder(self, msg="Pre-order : "):
        print(msg, end=' ')
        self.preorder(self.getRoot())
        print()

    def preorder(self, n):
        if n is not None:
            print(f"({n})", end="->")
            self.preorder(n.getLeft())
            self.preorder(n.getRight())

    def preorder2(self, n):
        s = LifoQueue()
        s.put(n)
        while not s.empty():
            n1 = s.get()
            if n1 is not None:
                print(n1, end=" ")
                s.put(n1.getLeft())
                s.put(n1.getRight())
        print()


    def printPostorder(self, msg="Post-order : "):
        print(msg, end=' ')
        self.postorder(self.getRoot())
        print()

    def postorder(self, n):
        if n is not None:
            self.postorder(n.getLeft())
            self.postorder(n.getRight())
            print(f"({n})", end="->")

    def printLevelorder(self, msg="Level-order: "):
        print(msg, end=" ")
        self.levelorder(self.getRoot())

    def levelorder(self, n): # Breadth First Search
        q = Queue()
        q.put(n)
        print("level")
        while not q.empty():
            n = q.get()
            if n is not None:
                print(f"({n})", end= "->")
                q.put(n.getLeft())
                q.put(n.getRight())
        print("(END)", end="\n")
    def count_node(self, n):
        if n is None:
            return 0
        else:
            return 1+self.count_node(n.getLeft()) + self.count_node(n.getRight())
    def count_leaf(self, n):
        if n is None:
            return 0
        elif self.isLeaf(n):
            return 1
        else:
            return self.count_leaf(n.getLeft()) + self.count_leaf(n.getRight())

    def isLeaf(self, n):
        return n.getLeft() is None and n.getRight() is None

    def get_height(self, n):
        if n is None:
            return -1
        hleft = self.get_height(n.getLeft())
        hright = self.get_height(n.getRight())
        if hleft == None or hright == None:
            pass
        elif hleft > hright:
            return hleft + 1
        else:
            hright + 1