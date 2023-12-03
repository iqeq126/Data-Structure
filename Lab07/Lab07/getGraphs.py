from Graph import *
from SearchGraph import *


def Graph01():
    sg = SearchGraph()
    g = Graph(False)
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")
    v5 = Vertex("E")
    v6 = Vertex("F")
    v7 = Vertex("G")
    v8 = Vertex("H")

    e1 = Edge(v1, v2, 1)
    e2 = Edge(v1, v3, 1)
    e3 = Edge(v2, v4, 1)
    e4 = Edge(v3, v4, 1)
    e5 = Edge(v4, v6, 1)
    e6 = Edge(v3, v5, 1)
    e7 = Edge(v5, v7, 1)
    e8 = Edge(v5, v8, 1)
    e9 = Edge(v7, v8, 1)

    g.addVertex(v1)
    g.addVertex(v2)
    g.addVertex(v3)
    g.addVertex(v4)
    g.addVertex(v5)
    g.addVertex(v6)
    g.addVertex(v7)
    g.addVertex(v8)
    print("1. Connected Components")
    sg.findCC(g.getAdjList())
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    sg.findCC(g.getAdjList())
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)
    sg.findCC(g.getAdjList())
    g.addEdge(e7)
    g.addEdge(e8)
    g.addEdge(e9)
    sg.findCC(g.getAdjList())
    return g

def Graph02():
    sg = SearchGraph()
    g = Graph(False)
    v1 = Vertex("v1"); v2 = Vertex("v2"); v3 = Vertex("v3"); v4 = Vertex("v4"); v5 = Vertex("v5"); v6 = Vertex("v6"); v7 = Vertex("v7")

    g.addVertex(v1); g.addVertex(v2); g.addVertex(v3); g.addVertex(v4)
    g.addVertex(v5);    g.addVertex(v6); g.addVertex(v7)

    sg.findCC(g.getAdjList())
    e1 = Edge(v1, v2, 2); e2 = Edge(v1, v3, 4); e3 = Edge(v1, v4, 1)
    e4 = Edge(v2, v4, 3); e5 = Edge(v2, v5, 10); e6 = Edge(v3, v4, 2)
    e7 = Edge(v3, v6, 5); e8 = Edge(v4, v5, 7); e9 = Edge(v4, v6, 8)
    e10 = Edge(v4, v7, 4); e11 = Edge(v5, v7, 6); e12 = Edge(v6, v7, 1)

    # print("1. Connected Components")
    g.addEdge(e1); g.addEdge(e2); g.addEdge(e3)
    sg.findCC(g.getAdjList())

    g.addEdge(e4); g.addEdge(e5); g.addEdge(e6)
    sg.findCC(g.getAdjList())

    g.addEdge(e7); g.addEdge(e8); g.addEdge(e9)
    sg.findCC(g.getAdjList())

    g.addEdge(e10); g.addEdge(e11); g.addEdge(e12)
    sg.findCC(g.getAdjList())
    return g


def Graph03():
    sg = SearchGraph()
    g = Graph(True)
    v1=Vertex("v1")
    v2=Vertex("v2")
    v3=Vertex("v3")
    v4=Vertex("v4")
    v5=Vertex("v5")
    v6=Vertex("v6")
    v7=Vertex("v7")

    g.addVertex(v1)
    g.addVertex(v2)
    g.addVertex(v3)
    g.addVertex(v4)
    g.addVertex(v5)
    g.addVertex(v6)
    g.addVertex(v7)

    e1 = Edge(v1, v2, 4); e2 = Edge(v1, v6, 10); e3 = Edge(v2, v1, 3); e4 = Edge(v2, v4, 18)
    e5 = Edge(v3, v2, 6); e6 = Edge(v4, v2, 5); e7 = Edge(v4, v5, 2); e8 = Edge(v4, v6, 19)
    e9 = Edge(v4, v7, 5); e10 = Edge(v5, v4, 1); e11 = Edge(v6, v7, 10); e12 = Edge(v7, v4, 8)
    e13 = Edge(v5, v3, 12); e14 = Edge(v4, v3, 15)
    print("1. Connected Components")
    sg.findCC(g.getAdjList())
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    sg.findCC(g.getAdjList())
    g.addEdge(e6)
    g.addEdge(e7)
    g.addEdge(e8)
    g.addEdge(e9)
    g.addEdge(e10)
    sg.findCC(g.getAdjList())
    g.addEdge(e11)
    g.addEdge(e12)
    g.addEdge(e13)
    g.addEdge(e14)
    sg.findCC(g.getAdjList())
    return g

def getGraph06():
    g = Graph(True)
    v1=Vertex("v1")
    v2=Vertex("v2")
    v3=Vertex("v3")
    v4=Vertex("v4")
    v5=Vertex("v5")
    v6=Vertex("v6")
    v7=Vertex("v7")

    g.addVertex(v1)
    g.addVertex(v2)
    g.addVertex(v3)
    g.addVertex(v4)
    g.addVertex(v5)
    g.addVertex(v6)
    g.addVertex(v7)

    e1 = Edge(v1, v2, 4); e2 = Edge(v1, v6, 10); e3 = Edge(v2, v1, 3); e4 = Edge(v2, v4, 18)
    e5 = Edge(v3, v2, 6); e6 = Edge(v4, v2, 5); e7 = Edge(v4, v5, 2); e8 = Edge(v4, v6, 19)
    e9 = Edge(v4, v7, 5); e10 = Edge(v5, v4, 1); e11 = Edge(v6, v7, 10); e12 = Edge(v7, v4, 8)
    e13 = Edge(v5, v3, 12); e14 = Edge(v4, v3, 15)

    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)
    g.addEdge(e7)
    g.addEdge(e8)
    g.addEdge(e9)
    g.addEdge(e10)
    g.addEdge(e11)
    g.addEdge(e12)
    g.addEdge(e13)
    g.addEdge(e14)

    return g


def getGraph05():
    sg = SearchGraph()
    g = Graph(False)
    v1 = Vertex("v1"); v2 = Vertex("v2"); v3 = Vertex("v3"); v4 = Vertex("v4"); v5 = Vertex("v5"); v6 = Vertex("v6"); v7 = Vertex("v7")#; v8 = Vertex("v8")

    g.addVertex(v1); g.addVertex(v2); g.addVertex(v3); g.addVertex(v4)
    g.addVertex(v5);    g.addVertex(v6); g.addVertex(v7)

    sg.findCC(g.getAdjList())

    e1 = Edge(v1, v2, 2); e2 = Edge(v1, v3, 4); e3 = Edge(v1, v4, 1)
    e4 = Edge(v2, v4, 3); e5 = Edge(v2, v5, 10); e6 = Edge(v3, v4, 2)
    e7 = Edge(v3, v6, 5); e8 = Edge(v4, v5, 7); e9 = Edge(v4, v6, 8)
    e10 = Edge(v4, v7, 4); e11 = Edge(v5, v7, 6); e12 = Edge(v6, v7, 1)

    g.addEdge(e1); g.addEdge(e2); g.addEdge(e3)
    sg.findCC(g.getAdjList())

    g.addEdge(e4); g.addEdge(e5); g.addEdge(e6)
    sg.findCC(g.getAdjList())

    g.addEdge(e7); g.addEdge(e8); g.addEdge(e9)
    sg.findCC(g.getAdjList())

    g.addEdge(e10); g.addEdge(e11); g.addEdge(e12)
    sg.findCC(g.getAdjList())
    print("Do Topological Search")
    sg.doTS(g.getAdjList())
    return g

class getGraphs:

    def getG6(self):
        sg = SearchGraph()
        g=Graph(False)
        v1 = Vertex("v1"); v2 = Vertex("v2"); v3 = Vertex("v3"); v4 = Vertex("v4")
        v5 = Vertex("v5"); v6 = Vertex("v6"); v7 = Vertex("v7"); v8 = Vertex("v8")

        g.addVertex(v1); g.addVertex(v2); g.addVertex(v3); g.addVertex(v4)
        g.addVertex(v5); g.addVertex(v6); g.addVertex(v7)

        sg.findCC(g.getAdjList())
        e1 = Edge(v1, v2, 2); e2 = Edge(v1, v3, 4); e3 = Edge(v1, v4, 1)
        e4 = Edge(v2, v4, 3); e5 = Edge(v2, v5, 10); e6 = Edge(v3, v4, 2)
        e7 = Edge(v3, v6, 5); e8 = Edge(v4, v5, 7); e9 = Edge(v4, v6, 8)
        e10 = Edge(v4, v7, 4); e11 = Edge(v5, v7, 6); e12 = Edge(v6, v7,1)

        g.addEdge(e1);  g.addEdge(e2);  g.addEdge(e3)
        sg.findCC(g.getAdjList())

        g.addEdge(e4);  g.addEdge(e5);  g.addEdge(e6)
        sg.findCC(g.getAdjList())

        g.addEdge(e7);  g.addEdge(e8);  g.addEdge(e9)
        sg.findCC(g.getAdjList())

        g.addEdge(e10);  g.addEdge(e11);  g.addEdge(e12)
        sg.findCC(g.getAdjList())
        return g
    def getG5(self):
        g = Graph(True)
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)

        e1 = Edge(v1, v2, 1)
        e2 = Edge(v1, v3, 1)
        e3 = Edge(v2, v4, 1)
        e4 = Edge(v2, v5, 1)
        e5 = Edge(v3, v4, 1)
        e6 = Edge(v4, v5, 1)

        g.addEdge(e1)
        g.addEdge(e2)
        g.addEdge(e3)
        g.addEdge(e4)
        g.addEdge(e5)
        g.addEdge(e6)

        return g

    def getG1(self):
        sg = SearchGraph()
        g = Graph(False)


        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")
        v6 = Vertex("F")
        v7 = Vertex("G")
        v8 = Vertex("H")

        sg.findCC(g.getAdjList())
        e1 = Edge(v1, v2, 1)
        e2 = Edge(v1, v3, 1)
        e3 = Edge(v2, v4, 1)
        e4 = Edge(v3, v4, 1)
        e5 = Edge(v4, v6, 1)

        sg.findCC(g.getAdjList())
        e6 = Edge(v3, v5, 1)
        e7 = Edge(v5, v7, 1)
        e8 = Edge(v5, v8, 1)
        e9 = Edge(v7, v8, 1)

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)
        g.addVertex(v6)
        g.addVertex(v7)
        g.addVertex(v8)

        g.addEdge(e1)
        g.addEdge(e2)
        g.addEdge(e3)
        g.addEdge(e4)
        g.addEdge(e5)
        g.addEdge(e6)
        g.addEdge(e7)
        g.addEdge(e8)
        g.addEdge(e9)

        return g

    def getG2(self):
        g=Graph(False)
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)

        e1 = Edge(v1, v2, 13)
        e2 = Edge(v1, v3, 10)
        e3 = Edge(v3, v4, 27)
        e4 = Edge(v2, v4, 25)
        e5 = Edge(v4, v5, 34)
        e6 = Edge(v2, v5, 18)

        g.addEdge(e1)
        g.addEdge(e2)
        g.addEdge(e3)
        g.addEdge(e4)
        g.addEdge(e5)
        g.addEdge(e6)

        return g