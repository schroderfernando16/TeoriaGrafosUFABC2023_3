#Fernando Schroder RA:11201921885

#Usando POO para uma programação mais clara e código limpo
class Disjuntos:
    def __init__(self):
        self.set = []

    def __init__(self, vertices):
        self.parent = list(range(vertices))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

#impelemntação de Kruskal baseado no que foi visto em aula
def kruskal(vertices, edges):
    ds = Disjuntos(vertices)
    mst_edges = []
    edges.sort(key=lambda x: x[2])  # arestas organizadas por peso

    for edge in edges:
        u, v, w = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append([u, v, w])

    return mst_edges

#main
n, m = map(int, input("").split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst_edges = kruskal(n, edges)
print('[', end='')
aux = 0
for edge in mst_edges:
    print(edge,end="")
    if aux < len(mst_edges)-1:
        print(",",end='')
    aux= aux + 1
print(']')
