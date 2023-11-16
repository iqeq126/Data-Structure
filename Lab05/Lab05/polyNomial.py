from DoublyLinkedList import *
class Term:
    def __init__(self, sgn=None, coeff=None, expon=None):
        self.sgn = sgn
        self.coeff = coeff
        self.expon = expon

    def __str__(self):
        return str(self.sgn) + str(self.coeff) + "x^"+ str(self.expon) + " "

    def getCoeff(self):
        return self.coeff

    def getExpon(self):
        return self.expon

    def getSyn(self):
        return self.sgn

class SparsePoly(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def display(self, msg=""):
        print("\t", msg, end='')

        node = self.head
        while node is not None:
            print(node, end='')
            node = node.getNext()
        print()

    def read(self):
        self.clear()
        while True:
            token = input("input term (syn coeff expon)").split(" ")
            if token[0] == '-1':
                self.display("The Polynomial : ")
                return
            self.addAt(self.getSize(), Term(token[0], float(token[1]), int(token[2])))

    def add(self, B):
        C = SparsePoly()
        a = self.head
        b = B.head

    def sub(self, B):
        pass

    def getDegree(self):
        pass