#Fernando Schroder Rodrigues RA: 11201921885

def transpose_graph(n, edges):

    # Criando o grafico para transpor a partir do primeiro grafo através de uma nova lista
    transposed = [[] for _ in range(n)]

    # Para cada aresta, invertemos a direção da orientação do grafo (U -> V teremos V->U)
    for u, v in edges:
        transposed[v].append(u)

    return transposed

#Aqui cria-se a lista para ser printada das adjacências do grafo transposto
def print_transposed_graph(transposed):
    for i, neighbors in enumerate(transposed):
        neighbors_str = ' '.join(map(str, neighbors))
        print(f"{i}: {neighbors_str}")



n, m = map(int, input("").split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Transpose the graph and print its adjacency lists
transposed = transpose_graph(n, edges)
print_transposed_graph(transposed)