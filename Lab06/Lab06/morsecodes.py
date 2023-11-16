from binaryNode import binaryNode
from binaryTree import binaryTree
from queue import Queue
class MorseCodes:
    def __init__(self):
        self.root = binaryNode()
        self.table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
                      ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
                      ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                      ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
                      ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
                      ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
                      ('Y', '-.--'), ('Z', '--..'),('0','-----'),('1','.----'),
                      ('2', '..---'), ('3','...--'), ('4','....-'),('5','.....'),
                      ('6','-....'),('7','--...'),('8','---..'),('9','---.')]

    def makeMorseTree(self):
        for tp in self.table:
            code = tp[1]
            node = self.root
            for c in code:
                if c == '.':
                    if node.getLeft() is None:
                        node.setLeft(binaryNode())
                    node = node.getLeft()
                elif c == '-':
                    if node.getRight() is None:
                        node.setRight(binaryNode())
                    node = node.getRight()
            node.setData(tp[0])

    def printMorseTree(self):
        n = self.root
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n = queue.get()
            if n is not None:
                print(f"({n})", end='->')
                queue.put(n.getLeft())
                queue.put(n.getRight())

    def decode(self, code):
        node = self.root
        for c in code:
            if c == '.':
                node = node.getLeft()
            elif c == '-':
                node = node.getRight()
        return node.data

    def encode(self, ch):
        if 'A' <= ch <= 'Z':
            idx = ord(ch) - ord('A')
            return self.table[idx][1]
        else:
            idx = ord(ch) - ord('0')
            return self.table[26+idx][1]