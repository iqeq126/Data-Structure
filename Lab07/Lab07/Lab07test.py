from getGraphs import getGraphs, getGraph06, Graph02, Graph03, Graph01, getGraph05
from SearchGraph import SearchGraph, EightQueens
from mst import MST, Dijkstra
def G1Test():
    g = Graph01()
    print(g)
    print(g.getEdges())
    M = g.getAdjMat()
    for i in M:
        print(i)
def G2Test():
    g = Graph02()
    print(g)
    print(g.getEdges())
    M=g.getAdjMat()
    for i in M:
        print(i)
    g.printAdjList()
def G3Test():
    g = Graph03()
    print(g)
    print(g.getEdges())
    M = g.getAdjMat()
    for i in M:
        print(i)
    g.printAdjList()
def GraphTest():
    print(f"G1Test()")
    G1Test()
    print(f"----------------------------------------------------\nG2Test()")
    G2Test()
    print(f"----------------------------------------------------\nG3Test()")
    G3Test()
def useDijkstra():
    g = Graph03()
    print(g)
    sv = g.getVertexList()[0]
    dk = Dijkstra()
    dk.runDijkstra(g, sv)
def useMST():
    mst = MST()
    g=Graph02()
    print(g)
    g.printAdjList()
    g.printAdjMat()
    mst=MST()
    T = mst.mstKruskal(g)
    print("Print Kruskal's graph\n", T)
    print(T)
    print(f"kruskal's getOrder() : {T.getOrder()}")
    print(f"kruskal's getSize() : {T.getSize()}")
    print(f"kruskal's getWeight() : {T.getWeight()}")
    print(f"kruskal's getEdgeList() : {T.getEdgeList()}")
    print("End Kruskal's Algorithm")

    print("Start Prim's Algorithm")
    g2 = Graph03()
    sv = g2.getVertexList()[0]
    T2 = MST.mstPrim(g2.isDirected(), g2, sv)
    print(T2)
    print(f"prim's getOrder() : {T2.getOrder()}")
    print(f"prim's getSize() : {T2.getSize()}")
    print(f"prim's getWeight() : {T2.getWeight()}")
    print(f"prim's getEdgeList() : {T2.getEdgeList()}")
    print("End Prim's Algorithm")
def useSearchGraph():
    sg = SearchGraph()
    print("Graph01")
    g1 = Graph01()
    adjList = g1.getAdjList()
    sv = g1.getVertexList()[0]
    sg.dfs(adjList, sv); print()
    sg.bfs(adjList, sv); print()
    al1 = g1.getAdjList()
    print("2. Do Topological Sort")
    sg.doTS(al1)
    print("--------------------------")
    print("Graph02")
    g2 = Graph02()
    adjList = g2.getAdjList()
    sv = g2.getVertexList()[0]
    sg.dfs(adjList, sv); print()
    sg.bfs(adjList, sv); print()
    al2 = g2.getAdjList()
    print("2. Do Topological Sort")
    sg.doTS(al2)
    print("--------------------------")
    print("Graph03")
    g3 = Graph03()
    adjList = g3.getAdjList()
    sv = g3.getVertexList()[0]
    sg.dfs(adjList, sv); print()
    sg.bfs(adjList, sv); print()
    al3 = g3.getAdjList()
    print("2. Do Topological Sort")
    sg.doTS(al3)
    print("--------------------------")
    print("3. N-Queens")
    for i in range(1,11):
        print(f"{i}-Queens : ", end =""); EightQueens(i).solve()

def main():
    #G1Test()
    print("----------------------------------------------------")
    #GraphTest() # Task-1
    # useSearchGraph() # Task-2
    # useMST() # Task-3
    useDijkstra() # Task-4

if __name__ == "__main__":
    main()
