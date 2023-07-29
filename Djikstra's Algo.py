
class Graph():

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)]
                    for row in range(vertex)]

    def Sol_print(self, d,check):
        print("Vertex \t Distance from Source\t\tOptimal Path")
        for node in range(self.V):
            path=[]
            self.Path_print(check,node,path)
            print(node, "\t\t", d[node],"\t\t\t", "->".join(path))

    def Path_print(self, check, n, path):
        if check[n]==-1:
            path.append(str(n))
            return
        self.Path_print(check,check[n],path)
        path.append(str(n))


    def d_min(self, d, set_sptree):	
        min = 1e7

        for v in range(self.V):
            if d[v] < min and set_sptree[v] == False:
                min = d[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        d = [1e7] * self.V
        d[src] = 0
        set_sptree = [False] * self.V
        check= [-1] * self.V


        for cout in range(self.V):


            u = self.d_min(d, set_sptree)

            set_sptree[u] = True


            for v in range(self.V):
                if (self.graph[u][v] > 0 and set_sptree[v] == False and d[v] > d[u] + self.graph[u][v]):
                    d[v] = d[u] + self.graph[u][v]
                    check[v]=u

        self.Sol_print(d,check)

g = Graph(7)
g.graph = [[0, 6, 5, 5, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 1, 0, 0],
        [0, 0, 2, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0]]

g.dijkstra(0)


