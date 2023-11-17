#Fernando Schroder RA:11201921885

import heapq

#Usando POO para uma programação mais clara e código limpo
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w)) #Assumindo um grafo não direcionado
    #Implementando prim, similar ao que foi passado em aula
    def prim_mst(self, root):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        visited = [False] * self.V
        key[root] = 0
        pq = [(0, root)]

        while pq:
            weight, u = heapq.heappop(pq)
            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v] and key[v] > w:
                    key[v] = w
                    parent[v] = u
                    heapq.heappush(pq, (w, v))

        return key, parent
#função main
n, m, r = map(int, input().split())
graph = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

keys, parents = graph.prim_mst(r)
print(keys)
print(parents)

