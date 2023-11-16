#Fernando Schroder Rodrigues - RA:11201921885


#Cria um grafo com peso naseado na entrada pelo teclado
def create_weighted_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
    return graph
#função para formatar a saída de acordo com o que é pedido no exercicio
def print_weighted_graph(graph):
    for u, neighbors in enumerate(graph):
        neighbors_str = ' '.join(f"{v}({w})" for v, w in neighbors)
        print(f"{u}: {neighbors_str}")

#Main
n, m = map(int, input("").split())
edges = []
print(f"")
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

graph = create_weighted_graph(n, edges)
print_weighted_graph(graph)

