from bstTree import *
class Record:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __eq__(self, other): return self.word == other.word
    def __ne__(self, other): return self.word != other.word
    def __lt__(self, other): return self.word < other.word
    def __gt__(self, other): return self.word > other.word

    def __str__(self): return "{}:{}".format(str(self.word), str(self.meaning))

class Dictionary(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def searchByWord(self, word):
        if word is not None:
            print("Record is -->> ", word)
        else:
            print("Your word is not found")

    def search_bst(self, key):
        n = self.search(self.getRoot(), key)
        if n is not None:
            print(" Item found : " + str(n.getData()))
        else:
            print(" Item not found " + str(key))

    def runDict(self):
        wdict = Dictionary()
        while True:
            command = input("i-insert, d-delete, p-print, s-search, q-quit ->")

            if command == 'i':
                word    = input(" > word: ").strip()
                meaning = input(" > meaning : ").strip()
                wdict.insert_bst(Record(word, meaning))

            elif command == 'd':
                word    = input("Inter word : ")
                wdict.delete_bst(Record(word, None))

            elif command == 'p':
                print(" Dictionary : ")
                wdict.inorder(wdict.root)
                print("\n")

            elif command == 's':
                word    = input(" > word : ").strip()
                n = wdict.search(wdict.root, Record(word, None))
                self.searchByWord(n)

            elif command == "q" : return
            else:
                print("It is not correct command!!")