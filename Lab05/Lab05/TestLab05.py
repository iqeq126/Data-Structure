from singlylinedlist import *
from LineEditor import *
from polyNomial import *
from DoublyLinkedList import *
from JosephusProblem import *
from circularLinkedList import *

def testJosephusProblem():
    jp = JosephusProblem(10, 3)
    jp.runJosephus()

def testCircularLinkedList():
    lst = CircularLinkedList()
    print(lst.getSize())
    lst.addFront(30)
    lst.addFront(15)
    print(lst)
    print(lst.getSize())
    lst.addFront(35)
    lst.addFront(20)
    lst.addFront(22)
    lst.addFront(25)
    lst.addFront(50)
    lst.addRear(150)
    lst.addRear(250)
    print(lst)
    print("deleted -> ", lst.deleteFront())
    print(lst)
    print("deleted -> ", lst.deleteRear())
    print(lst)
    print("deleted -> ", lst.deleteAt(3))
    # print("position -> ", lst.findPos(lst.head.next), lst.head.next)
    print("position -> ", lst.findPos(lst.head), lst.head)
    print(lst)

def testDoublyLinkedList():
    lst2 = DoublyLinkedList()
    print(lst2.getSize())

    lst2.addRear(30)
    lst2.addRear(35)
    lst2.addFront(47)
    print(lst2)
    print(lst2.getSize())
    lst2.addFront(50)
    lst2.addRear(40)
    lst2.addFront(55)
    lst2.addRear(60)
#   lst2.addFront(70)
    lst2.addAt(3, 70)
#   lst2.addRear(80)
    lst2.addAt(3, 80)
    print(lst2)
    print("deleted -> ", lst2.deleteFront())
    print("deleted -> ", lst2.deleteRear())
    print("deleted -> ", lst2.deleteAt(2))
    print("deleted -> ", lst2.deleteAt(2))

    print(lst2)

def testNodes():
    d = Node(100, None)
    c = Node(99, d)
    b = Node(23, c)
    a = Node(None, b)

    print(a, a.getNext(), a.getNext().getNext(), a.getNext().getNext().getNext())
    print(a, a.next, a.next.next, a.next.next.next)

def testSinglyLinkedList():
    lst = SinglyLinkedList()

    lst.addAt(0, 10)
    lst.addAt(0, 20)
    lst.addAt(1, 30)
    lst.addAt(lst.getSize(), 40)
    lst.addAt(2, 50)
    lst.addFront(23)
    lst.addRear(25)
    lst.printList("Element in the List : ")
    print(lst.getDataAt(2))
    lst.replaceDataAT(2, 90)
    print("List after replacing 2nd element : ", lst)
    lst.reverseList()
    print("List after reversing : ", lst)
    print(lst.deleteFront())
    print("List after deleting element from front : ", lst)
    print(lst.deleteRear())
    print("List after deleting element from Rear : ", lst)
    print(lst.deleteAt(2))
    print("List after deleting 2nd element : ", lst)
    print(lst.deleteAt(0))
    print("List after deleting 3rd element : ", lst)
    lst.deleteAt(lst.getSize())
    print("List after deleting 3rd element : ", lst)
    lst.clear()
    print(lst)

def testPoly():
    a = SparsePoly()
    b = SparsePoly()
    a.read()
    b.read()
    #c = a.add(b)
    a.display(" A = ")
    b.display(" B = ")
    #c.display(" A + B = ")
def main():
    # le = LineEditor()
    # le.runLineEditor()
    # testNodes()
    # testSinglyLinkedList()
    # le.runLineEditor()
    # testPoly()
    # testDoublyLinkedList()
    testJosephusProblem()
    # testCircularLinkedList()
if __name__ == "__main__":
    main()