from queue import PriorityQueue
from Graph import Graph
from DisjointSet import DisjointSet as DS


class Dijkstra:
    def runDijkstra(self, G, src):
        Known = {}
        Dv = {}
        Pv = {}
        for vtx in G.getVertexList():
            Known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None
        Known[src] = True
        Dv[src] = 0.0
        PQ = PriorityQueue()
        PQ.put((0, src))
        EdgeDistance = 0.0
        newDistance = 0.0

        while not PQ.empty():
            emin = PQ.get()[1]
            for e in G.getNeighborEdges(emin):
                EdgeDistance = e.getW()
                newDistance =Dv[e.getU()]+ EdgeDistance
                if not Known[e.getV()] and Dv[e.getV()] > newDistance:
                    Dv[e.getV()] = newDistance
                    Pv[e.getV()] = newDistance
                    PQ.put((newDistance, e.getV()))
                Known[e.getU()] = True
    def printConfigration(self, Known, Dv, Pv):
        print("Configration")
        for vtx in Known:
            print(f"{vtx}, {Known[vtx]}, {Dv[vtx]}, {Pv[vtx]}")

class MST:
    def mstKruskal(self, g):
        T = Graph(g.isDirected())
        for v in g.getVertexList():
            T.addVertex(v)
        ds = DS()
        for v in g.getVertexList():
            ds.makeSet(v)
        pq = PriorityQueue()
        for e in g.getEdges():
            pq.put(e)

        numberOfEdges = 0
        while not pq.empty():
            e = pq.get()
            p1 = ds.find(e.getU())
            p2 = ds.find(e.getV())
            if p1 != p2:
                T.addEdge(e)
                ds.Union(p1, p2)
                numberOfEdges += 1
        return T
    def mstPrim(self, G, src):
        T = Graph(G.isDirected())
        eList = []

        PQ = PriorityQueue()
        for e in G.getNeighborEdges(src):
            PQ.put(e)
        T.addVertex(src)

        while T.getOrder() != G.getOrder():
            minE = PQ.get()
            vtxV = minE.getV()
            if vtxV in T.getVertexList():
                continue
            T.addVertex(vtxV)
            eList.append(minE)
            for e in G.getNeighborEdges(vtxV):
                PQ.put(e)
                T.addEdge(e)

        for e in eList:
            print(e)

        return T
