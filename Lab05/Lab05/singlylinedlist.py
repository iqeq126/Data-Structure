from node import *

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, data):
        new_node = Node(data) # create a new node
        if self.head:
            new_node.next = self.head # link new_node to heaf
        self.head = new_node # make new_node as head

    def addRear(self, data):
        if self.head is None:
            self.insertFront(data) # if this is first node,

        else:
            temp = self.head
            while temp.next: # traverse to last node
                temp = temp.next
            temp.next = Node(data)

    def addAt(self, pos, data):
        before = self.getNodeAt(pos-1)
        if before == None: # if it is the last node
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.next)
            before.next = node
    def deleteFront(self): # delete from head
        tmp = self.head
        if self.head:
            self.head = self.head.next
            tmp.next = None
        return tmp

    def deleteRear(self): # delete from tail
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next

                second_last = tmp
                tmp = tmp.next
                second_last.next = None
        return tmp

    def deleteAt(self, pos):
        tmp = Node()
        if self.isEmpty() or pos > self.getSize():
            tmp = None
        elif pos == 0:
            tmp = self.deleteFront()
        elif pos == self.getSize():
            tmp = self.deleteRear()
        else:
            prev = self.getNodeAt(pos -1)
            tmp = prev.next
            prev.next = tmp.next
            tmp.next = None
        return tmp

    def getNodeAt(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node

    # print every node data
    def printList(self, msg = "Singly Linked List : ") -> None:
        print(msg, end='')
        tmp = self.head
        while tmp:
            print(tmp.data, end = "->")
            tmp = tmp.next
        print("END")

    def __str__(self):  # String representataion
        tmp = self.head
        string_repr = ""
        while tmp:
            string_repr += str(tmp) + "->"
            tmp = tmp.next
        return string_repr + "END"

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node == None:
            return None
        else:
            return node.getData()

    def replaceDataAT(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data =data

    def isEmpty(self) -> bool:
        return self.head == None # return True if head is None

    def clear(self):
        self.head = None

    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.getNext()
            count += 1
        return count

    def reverseList(self):
        prev = None
        tmp = self.head

        while tmp:
            next_node = tmp.next # Store the current node's next node
            tmp.next = prev # Make the current node's next point backwards
            prev = tmp # Make the previous node be the current node
            tmp = next_node # Make the current node the next node(to progress iteration)
            self.head = prev # Return prev in order to put the head at the end

    def findData(self, val):
        node = self.head
        while node is not None:
            if node.data == val : return node
            node = node.next
        return node

    def printByLine(self):
        print("Line Editor")
        node = self.head
        line = 0
        while node is not None:
            #print("[%2d] "%line, end='')
            print(f"{line} = {node}")
            # print(node)
            node = node.next
            line += 1
        print()

