from queueADT import *
from Stack import *
class Cell:
    def __init__(self, r, c):
        self.row = r
        self.col = c
    def __str__(self):
        return '(' + str(self.row) + ", " + str(self.col) + ")"
class Maze:
    MAZE_SIZE = 6
    def getMap(self):
        _map = [ ['1','1','1','1','1','1'],
                ['e','0','1','0','0','1'],
                ['1','0','0','0','1','1'],
                ['1','0','1','0','1','1'],
                ['1','0','1','0','0','x'],
                ['1','1','1','1','1','1']]
        return _map

    def isValidPos(self, x, y, _map):
        if (x < 0 or y < 0 or x >= self.MAZE_SIZE or y >= self.MAZE_SIZE):
            return False
        else:
            return _map[y][x] == '0' or _map[y][x] == 'x'

    def DFS1(self):
        _map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0,1)
        deq.addFront(entry)
        print("\nDFS1: Using Deque Data Structure : ")

        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end="->")
            x = here.row
            y = here.col
            if (_map[y][x] == 'x') : return True
            else:
                _map[y][x] = '.'
                if self.isValidPos(x-1, y, _map) : deq.addFront(Cell(x-1, y))
                if self.isValidPos(x+1, y, _map) : deq.addFront(Cell(x+1, y))
                if self.isValidPos(x, y-1, _map) : deq.addFront(Cell(x, y-1))
                if self.isValidPos(x, y+1, _map) : deq.addFront(Cell(x, y+1))
        return False

    def DFS2(self):
        _map = self.getMap()
        s = Stack()
        entry = Cell(0,1)
        s.push(entry)
        print("\nDFS2 : using Stack Data Structure : ")

        while (s.isEmpty() == False):
            here = s.pop()
            print(here, end="->")
            x = here.row
            y = here.col
            if (_map[y][x]=='x'): return True
            else:
                _map[y][x] = '.'
                if self.isValidPos(x - 1, y, _map): s.push(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, _map): s.push(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, _map): s.push(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, _map): s.push(Cell(x, y + 1))
        return False

    def DFS3(self):
        _map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print("\nDFS3: Using Deque Data Structure : ")

        while not deq.isEmpty():
            here = deq.deleteRear()
            print(here, end = "->")
            x = here.row
            y = here.col
            if _map[y][x] == 'x': return True
            else:
                _map[y][x] = '.'
                if self.isValidPos(x - 1, y, _map): deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, _map): deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, _map): deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, _map): deq.addRear(Cell(x, y + 1))
        return False

    def BFS1(self):
        _map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print("\nBFS1 : using Deque Data Structure: ")
        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end="->")
            x = here.row
            y = here.col
            if _map[y][x] == 'x':
                return True
            else:
                _map[y][x] = '.'
                if self.isValidPos(x - 1, y, _map): deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, _map): deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, _map): deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, _map): deq.addRear(Cell(x, y + 1))
        return False

    def BFS2(self):
        _map = self.getMap()
        que = CircularQueue()
        entry = Cell(1, 0)
        que.enqueue(entry)
        print("\nBFS2 : using Queue Data Structure: ")

        while not que.isEmpty():
            here = que.dequeue()
            print(here, end="->")
            x = here.row
            y = here.col
            if _map[y][x] == 'x':
                return True
            else:
                _map[y][x] = '.'
                if self.isValidPos(x, y - 1, _map): que.enqueue(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, _map): que.enqueue(Cell(x, y + 1))
                if self.isValidPos(x - 1, y, _map): que.enqueue(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, _map): que.enqueue(Cell(x + 1, y))
        return False