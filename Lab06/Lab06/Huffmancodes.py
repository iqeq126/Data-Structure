from minheap import *
class HNode:
    def __init__(self, char=None, freq=None, left =None, right =None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right =right

    def __str__(self): return str(self.freq)
    def __eq__(self, other): return self.freq == other.freq
    def  __ne__(self, other): return self.freq != other.freq
    def __lt__(self, other): return self.freq < other.freq
    def __le__(self, other): return self.freq <= other.freq
    def __gt__(self, other): return self.freq > other.freq
    def __ge__(self, other): return self.freq >= other.freq
class Huffman():
    def __init__(self, txt=None):
        self.text = txt
        self.mh = MinHeap()
        self.codes = {}
        self.decodes = {}

    def makeCodes(self):
        root = self.makeHuffmanTree()
        current_code = ""
        self.make_codes(root, current_code)

    def make_codes(self, root, current_code):
        if root is None:
            return

        if root.char != None:
            self.codes[root.char] = current_code
            self.decodes[current_code] = root.char
            return

        self.make_codes(root.left, current_code + "0")
        self.make_codes(root.right, current_code + "1")

    def makeHeap(self):
        frequencies = self.makeFrequencyDict()
        for key in frequencies:
            node = HNode(key, frequencies[key])
            self.mh.insert(node)

    def makeFrequencyDict(self):
        frequencies = {}
        for c in self.text:
            if not c in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
        return frequencies

    def makeHuffmanTree(self):
        self.makeHeap()
        while self.mh.getSize() > 1:
            p, q = self.mh.delete(), self.mh.delete()
            r = HNode(None, p.freq + q.freq, p, q)
            self.mh.insert(r)
        return self.mh.delete()

    def getEncodeText(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def printCodes(self):
        self.makeCodes()
        for key in self.codes:
            print(f"{key} : {self.codes[key]}")

        print("Reverse Coding")
        for key in self.decodes:
            print(f"{key} : {self.decodes[key]}")