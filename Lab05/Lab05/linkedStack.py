from node import *
class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head: # create a new node
            new_node.next = self.head # link new_node to head
        self.head = new_node # make new_node as head

    def pop(self): # delete from head
        tmp = self.head
        if self.head:
            self.head = self.head.next
            tmp.next = None
        return tmp

    def __str__(self): # String representation
        tmp = self.head
        string_repr = ""
        while tmp:
            string_repr += str(tmp) + "->"
            tmp = tmp.next

        return string_repr + "END"

    def getNodeAt(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node == None:
            return None
        else:
            return node.getData()

    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data = data

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.getNext()
            count += 1
        return count

