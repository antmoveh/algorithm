

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

# Vertex: color {white: 未到达， gray: 已到达， black: 邻居遍历完成}
def bfs(g: Graph, start: Vertex):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert: Vertex = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            if nbr.id == "sage":
                return nbr
        currentVert.setColor("black")


def traverse(y: Vertex):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

g = Graph()
bfs(g, g.getVertex("fool"))
traverse(g.getVertex("sage"))