from singlylinedlist import *

class LineEditor:
    def __init__(self):
        self.lst = SinglyLinkedList()

    def runLineEditor(self):
        while True:
            command = input(f"i-insert, d- delete, r= replace, p- print, l- loadfile, s-writefile, q-quit ->")
            if command == 'i' : self.addLine()
            elif command == 'd' : self.deleteLine()
            elif command == 'r' : self.replaceLine()
            elif command == 'p' : self.printByLine()
            elif command == 'l' : self.loadFromFile()
            elif command == 's' : self.writeToFile()
            elif command == 'q' : return

    def addLine(self):
        pos = int(input("input line number : "))
        _str = input(" input line text ")
        self.lst.addAt(pos, _str)

    def deleteLine(self):
        pos = int( input("input line number : "))
        self.lst.deleteAt(pos)

    def replaceLine(self):
        pos = int( input("input linen number : "))
        _str = input("input modified text : ")
        self.lst.replaceDataAT(pos, _str)

    def printByLine(self):
        self.lst.printByLine()

    def loadFromFile(self):
        # filename = input("read from file")
        filename = "test.txt"
        with open(filename, "r") as infile:
            lines = infile.readlines()
            for line in lines:
                self.lst.addAt(self.lst.getSize(), line.rstrip('\n'))
                print(line, end="")

    def writeToFile(self):
        # filename = input("write to file")
        filename = "test.txt"
        with open(filename, "w") as outfile:
            sz = self.lst.getSize()
            # print(sz)
            for i in range(sz):
                outfile.write(self.lst.getDataAt(i) + '\n')

