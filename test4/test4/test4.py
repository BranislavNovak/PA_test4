import sys
import math

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, d1 = None, d2 = math.inf):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.p = None
        self.d1 = d1
        self.d2 = d2
        self.list = list()

class Edge:
    def __init__(self, source = None, destination = None, weight = None):
        self.source = source;
        self.destination = destination
        self.weight = weight

def MakeGraph():
    vertex_list = list()
    
    a = Vertex(d1 = 'a')
    b = Vertex(d1 = 'b')
    c = Vertex(d1 = 'c')
    d = Vertex(d1 = 'd')
    e = Vertex(d1 = 'e')
    f = Vertex(d1 = 'f')
    g = Vertex(d1 = 'g')
    h = Vertex(d1 = 'h')

    a.list.append(Edge(a,b,3))
    a.list.append(Edge(a,e,2))
    vertex_list.append(a)
    
    b.list.append(Edge(b,c,6))
    b.list.append(Edge(b,h,3))
    vertex_list.append(b)   

    c.list.append(Edge(c,d,3))
    vertex_list.append(c)    

    e.list.append(Edge(e,f,2))
    vertex_list.append(e)    

    f.list.append(Edge(f,g,4))
    f.list.append(Edge(f,h,3))
    vertex_list.append(f)

    h.list.append(Edge(h,d,4))
    h.list.append(Edge(h,f,3))
    vertex_list.append(h)

    g.list.append(Edge(g,d,4))
    vertex_list.append(g)

    vertex_list.append(d)

    return vertex_list

def PrintGraph(graph):
    for i in graph:
        print("--->", i.d1)
        for j in i.list:
            print("------>", j.destination.d1, j.weight)

def Initialize_single_source(G,s):
    for v in G:
        v.d2 = math.inf
        v.p = None
    s.d2 = 0

def Relax(u,v,w):
    if v.d2 > u.d2 + w:
        v.d2 = u.d2 + w
        v.p = u

def Extract_min(Q):
    min = 0
    for i in range (len(Q)):
        if Q[i].d2 <= Q[min].d2:
            min = i
    ret = Q.pop(min)
    return ret

def Dijkstra(G,w,s):
    Initialize_single_source(G,s)
    S = list()
    Q = G[:]                                            # kopiram graph u pomocni
    while len(Q) is not 0:
        u = Extract_min(Q)
        S.append(u)
        for v in u.list:
            Relax(v.source, v.destination, v.weight)        

def ShortestPath(graph):
    shortest_path_list = list()
    A = graph[0]
    B = graph[len(graph)-1]    

    Dijkstra(graph, 0, A)
    w = B.d2
    parent = B.p
    shortest_path_list.append(B)

    while parent != A:
        shortest_path_list.append(parent)
        parent = parent.p
    shortest_path_list.append(A)
    shortest_path_list = shortest_path_list[::-1]

    return shortest_path_list,w  

def PrintPath(list):
    for i in list:
        print(i.d2, "-->", i.d1)

def UpdateEdge(graph, A, B, weight):
    already_exist = 0
    for i in A.list:
        if i.destination == B:
            i.weight = weight
            already_exist = 1
    if already_exist == 0:
        A.list.append(Edge(A,B,weight))

if __name__ == "__main__":

    vertex_list = list()
    shortest_path_list = list()

    print("\n------------------ MakeGraph() --------------------")
    vertex_list = MakeGraph()
    PrintGraph(vertex_list)

    print("\n------------------ ShortestPath() --------------------")
    shortest_path_list, w = ShortestPath(vertex_list)    
    PrintPath(shortest_path_list)

    print("\n------------------ UpdateEdge() + ShortestPath() --------------------")
    for i in vertex_list:
        if i.d1 == 'b':
            b = i
        elif i.d1 == 'h':
            h = i

    UpdateEdge(vertex_list, b, h, 5)
    shortest_path_list, w = ShortestPath(vertex_list)    
    PrintPath(shortest_path_list)
    
    

    

  
