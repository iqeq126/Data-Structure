from queue import Queue, LifoQueue
from Graph import Graph
from collections import defaultdict

class SearchGraph:
    def bfs(self, adjList, start):
        visited = set()
        print("BFS starting with Vertex ", start)
        visited.add(start)
        Q = Queue()
        Q.put(start)
        while not Q.empty():
            v = Q.get()
            print(v, end='->')
            nbr = adjList[v]
            for u in nbr:
                if u not in visited:
                    visited.add(u)
                    Q.put(u)

    def dfs(self, adjList, start, visited=set()):
        #if visited is None:
        #    visited = set()
        if start not in visited:
            visited.add(start)
            print(start, end=' ')
            for next in adjList[start] - visited:
                self.dfs(adjList, next, visited)

    def dfs(self, adjList, start):
        visited=set()
        print("DFS : Starting with Vertex ", start)
        visited.add(start)
        S = LifoQueue()
        S.put(start)
        while not S.empty():
            v = S.get()
            print(v, end="->")
            neighber = adjList[v]
            for u in neighber:
                if u not in visited:
                    visited.add(u)
                    S.put(u)
    #For task-2
    def doTS(self, adjList):
        visited = defaultdict()
        for vtx in adjList:
            visited[vtx] = False
        result = []
        for v in visited:
            self.dfsTS(v, adjList, visited, result)
        print(result)

    def dfsTS(self, v, adjList, visited, result):
        if not visited[v]:
            visited[v] = True
            for neighber in adjList[v]:
                self.dfsTS(neighber, adjList, visited, result)
            result.insert(0, v)
    # for task-2
    def findCC(self, adjList):
        visited = set()
        colonList = []

        for v in adjList:
            if v not in visited:
                colon = self.dfsCC(adjList, [], v ,visited)
                colonList.append(colon)
        print(f"Connected Components : {len(colonList)}")
        print(colonList)

    def dfsCC(self, adjList, colon, v, vistted):
        if v not in vistted:
            vistted.add(v)
            colon.append(v)
            n = adjList[v]
            for vtx in n:
                if vtx not in vistted:
                    self.dfsCC( adjList, colon, vtx, vistted)

        return colon
# For task-2
class EightQueens:
    def __init__(self, NQ):
        self.NQ = NQ
        self.solutions = 0
        self.NN =  0

    def solve(self):
        board = [-1] * self.NQ
        self.dfsPQ(board, 0)
        print("Found ", self.solutions, "solutions.")
        print("Nodes ", self.NN)


    def dfsPQ(self, board, row):
        if row == self.NQ: # if possible solution found
            #print(board)
            self.solutions += 1
        else:
            for col in range(self.NQ):
                if not self.isAttack(board, row, col):
                    self.NN += 1
                    board[row] = col
                    self.dfsPQ(board, row+1)


    def isAttack(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return True

        return False

