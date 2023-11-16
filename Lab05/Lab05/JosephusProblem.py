from circularLinkedList import *
class JosephusProblem:
    def __init__(self, n = 10, m = 3):
        self.lst = CircularLinkedList()
        self.n = n
        self.m = m
        for i in range(1, n + 1):
            self.lst.addFront(i)

    def runJosephus(self):
        print(self.lst)
        temp = self.lst.head.next
        count = 0
        while True:
            temp = temp.next
            count += 1

            if count == self.m:
                temp2 = temp.next
                pos = self.lst.findPos(temp)
                print("Eliminated -> ", self.lst.deleteAt(pos))
                temp = temp2
                print(self.lst)

                count = 0
            if temp == temp.next:
                print("Selected -> ", temp)
                break
