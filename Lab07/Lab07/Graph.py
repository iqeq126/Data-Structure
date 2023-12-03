from collections import OrderedDict
from DisjointSet import DisjointSet
class Graph:
    def __init__(self, directed = False, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict  = gdict
        self.directed = directed
        self.keyIndex = {}
    def isDirected(self):
        return self.directed

    def getVertexList(self):
        dict1 = OrderedDict(sorted(self.keyIndex.items()))
        return list(dict1.keys())

    def getOrder(self):
        return len(self.gdict.keys())

    def getEdgeList(self):
        eList = []
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                eList.append(e)
        return eList
    def getSize(self):
        size = len(self.getEdgeList())
        if not self.isDirected():
            size //= 2
        return size

    def getDegree(self, vtx): return self.getOutDegree(vtx), self.getInDegree(vtx)

    def getOutDegree(self,vtx): return len(self.gdict[vtx])

    def printOutDegree(self):
        for vtx in self.gdict:
            print(f"Out degree of vertex {vtx} = {self.getOutDegree(vtx)}")
    def getInDegree(self, vtx):
        return len(self.getInwardEdges(vtx))
    def getInwardEdges(self, vtx):
        eList = []
        for e in self.getEdgeList():
            if vtx == e.getV():
                eList.append(e)
        return eList

    def printInDegree(self):
        for vtx in self.gdict:
            print(f"Out degree of vertex {vtx} = {self.getInDegree(vtx)}")

    def printAdjList(self):
        aList = self.getAdjList()
        for vtx in aList:
            print(f"{vtx} : {aList[vtx]}")
    def getNeighborVertices(self, vtx):
        elist = self.gdict.get(vtx)
        vlist = []
        for e in elist:
            vlist.append(e.getV())
        return vlist

    def getNeighborEdges(self, vtx):
        return self.gdict[vtx]

    def getNeighbors(self, v):
        nList = []
        eList = self.gdict.get(v)
        for e in eList:
            nList.append(e.getV())
        return nList

    def getAdjList(self):
        aList = {}
        for vtx in self.gdict:
            aList[vtx] = set(self.getNeighbors(vtx))
        return aList

    def getEdges(self):
        eList = []
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                eList.append(e)
        return eList


    def getAdjMat(self):
        adjMat = [[0 for x in range(len(self.keyIndex))]for y in range(len(self.keyIndex))]
        for e in self.getEdges():
            adjMat[self.keyIndex[e.getU()] -1][self.keyIndex[e.getV()]-1] = e.getW()
        return adjMat

    def printAdjMat(self):
        print("\n Adjacency Matrix:")
        adjMatrix = self.getAdjMat()
        for i in range(len(self.keyIndex)):
            print()
            for j in range(len(self.keyIndex)):
                print("{0:>3d}".format(adjMatrix[i][j]), end="")
        print()

    def getWeight(self):
        w = 0
        for e in self.getEdgeList():
            w += e.getW()
        if not self.isDirected():
            w = w // 2
        return w

    def isCycle(self):
        cycle  =False
        ds = DisjointSet()
        for vtx in self.getVertexList():
            ds.makeSet(vtx)

        for e in self.getEdgeList():
            x = ds.find(e.getU())
            y = ds.find(e.getV())
            if x != y:
                ds.Union(x, y)
            else:
                return True
        return cycle
    def __repr__(self):
        gs =""
        for vtx in self.gdict:
            gs += f"{vtx} : {self.gdict[vtx]}\n"
        return gs

    def __str__(self):
        gs =""
        for vtx in self.gdict:
            gs += f"{vtx} : {self.gdict[vtx]}\n"
        return gs

    def addVertex(self, vtx):
        if vtx in self.gdict:
            print("Vertex is already added..")
        else:
            self.gdict[vtx] = []
            self.keyIndex[vtx] = len(self.keyIndex)+1

    def addEdge(self, e):
        if e.getU() in self.gdict:
            self.gdict[e.getU()].append(e)
        if not self.directed:
            e2 = Edge(e.getV(), e.getU(), e.getW())
            self.gdict[e2.getU()].append(e2)

class Edge:
    def __init__(self, u=None, v = None, w= None):
        self.u=u
        self.v=v
        self.w=w
    def getU(self):
        return self.u

    def getV(self):
        return self.v

    def getW(self):
        return self.w

    def setU(self, u):
        self.u =u

    def setV(self, v):
        self.v =v

    def setW(self, w):
        self.w = w
    def __str__(self):
        return f"( ({self.u}, {self.v}) -> {self.w} )"
    def __repr__(self):
        return f"( ({self.u}, {self.v}) -> {self.w} )"

    def __hash__(self):
        return hash(self.w)

    def __eq__(self, other):
        return self.w  == other.w

    def __ne__(self, other):
        return self.w != other.w

    def __lt__(self, other):
        return self.w < other.w

    def __le__(self, other):
        return self.w <= other.w

    def __gt__(self, other):
        return self.w > other.w

    def __ge__(self, other):
        return self.w >= other.w


class Vertex:
    def __init__(self, key = None):
        self.key = key

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def setData(self, k):
        self.key = k

    def getData(self):
        return self.key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key  == other.key

    def __ne__(self, other):
        return self.key != other.key
    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key