#Fernando Schroder Rodrigues RA:11201921885

import heapq

#Usando POO e classes para uma programação mais organizada
#Criando a classe grafo
class Graph:
    def __init__(self, vertices):
        #inicializando o grafo com vertices recebidos
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    #adicionando as arestas
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    #Implementação do algoritimo para definir o menor caminho entre as arestas/nós
    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        parents = [-1] * self.V
        distances[src] = 0
        pq = [(0, src)]

        while pq:
            dist, u = heapq.heappop(pq)

            for v, w in self.graph[u]:
                if distances[v] > dist + w:
                    distances[v] = dist + w
                    parents[v] = u
                    heapq.heappush(pq, (distances[v], v))

        return distances, parents


n, m, s = map(int, input().split())
graph = Graph(n)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

distances, parents = graph.dijkstra(s)
print(distances)
print(parents)

