#Lecture 11/29/18


class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        #if f is not in the graph, it will be added to the graph
        if f not in self.vertList:
            nv = self.addVertex(f)
        #same goes with t
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()
    #iterator function that will return the values of the vertices list
    def __iter__(self):
        return iter(self.vertList.values())




#Dijkstra's mapping algorithm

def dijkstra(Graph, V):
    unvisited = []
    visited = []
    dist = []
    prev = []
    for v in Graph:
        dist.append(99999999999999999)
        prev.append(None)
        unvisited.append(v)

    dist[V] = 0

    while len(unvisited) > 0:
        
        u = unvisited[min(dist)]
        unvisited.remove(u)

        #for each neighbor v of u:
        for n in u.getConnections():
            alt = dist[unvisited.index(u)] + u.getWeight(n)
            if alt < dist[unvisited.index(n)]:
                dist[unvisited.index(n)] = alt
                prev[unvisited.index(n)] = u

    return dist, prev
                    

def main():
    G = Graph()
    A = Vertex('A')
    G.addVertex('A')
    G.addVertex('B')
    G.addVertex('C')
    G.addVertex('D')
    G.addVertex('E')
    print(G.getVertices())
    G.addEdge('A', 'B', 'e4')
    G.addEdge('B','D','e3')
    G.addEdge('D','E', 'e2')
    G.addEdge('E','A', 'e1')
    G.addEdge('B','C', 'e5')
    G.addEdge('C','D', 'e6')
    for v in G:
        for n in v.getConnections():
            #the weird percent s things are just there to print the parenthesis, dont need it
            print("( %s , %s, %s )" % (v.getId(), n.getId(), v.getWeight(n)))
main()
