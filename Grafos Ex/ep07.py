#Fernando Schroder RA:11201921885


#algoritmo de busca em profundidade
def dfs(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.insert(0, v)

#Função para Transpor o Grafo
def transpose_graph(n, edges):
    transposed = [[] for _ in range(n)]
    for u, v in edges:
        transposed[v].append(u)
    return transposed

#Executa a DFS no grafo transposto
def dfs_transposed(graph, v, visited, component):
    visited[v] = True
    component.append(f"({v}")
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_transposed(graph, neighbor, visited, component)
    component.append(f"{v})")

#Verifica componentes fortemente conexos
def find_scc(n, edges):
    stack = []
    visited = [False] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    transposed = transpose_graph(n, edges)
    visited = [False] * n

    scc = []
    for v in stack:
        if not visited[v]:
            component = []
            dfs_transposed(transposed, v, visited, component)
            scc.append(component)

    return scc
#Formata a lista de acordo com a saída pedida no exercicio
def format_scc(scc):
    formatted_scc = []
    for component in scc:
        formatted_scc.append(' '.join(component))
    return ' '.join(formatted_scc)

#funcao main
n, m = map(int, input("").split())
edges = []
print(f"")
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

components = find_scc(n, edges)
formatted_components = format_scc(components)
print(formatted_components)
