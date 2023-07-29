
class Graph:

    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []

    def edge_Add(self, p, q, r):
        self.graph.append([p, q, r])

    def Bellman_Ford_Algo(self, src):

        d = [float("Inf")] * self.V
        check = [-1] * self.V
        d[src] = 0

        for _ in range(self.V - 1):

            for p, q, r in self.graph:
                if d[p] != float("Inf") and d[p] + r < d[q]:
                    d[q] = d[p] + r
                    check[q]=p


        for p, q, r in self.graph:
            if d[p] != float("Inf") and d[p] + r < d[q]:
                print("Graph contains negative weight cycle")
                return

        
        print("Vertex\t Distance\t Shortest Path")
        for i in range(self.V):
            print("{0}\t\t{1}\t\t".format(i, d[i]), end="")
            path = []
            dest = i
            while dest != src:
                path.append(dest)
                dest = check[dest]
            path.append(src)
            print(path[::-1])




g = Graph(7)
g.edge_Add(0, 1, 6)
g.edge_Add(0, 2, 5)
g.edge_Add(0, 3, 5)
g.edge_Add(2, 1, -2)
g.edge_Add(3, 2, -2)
g.edge_Add(1, 4, -1)
g.edge_Add(2, 4, 1)
g.edge_Add(3, 5, -1)
g.edge_Add(4, 6, 3)
g.edge_Add(5, 6, 3)

g.Bellman_Ford_Algo(0)


