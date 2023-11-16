#Fernando Schroder Rodrigues RA:11201921885

def dfs(graph, start_vertex, discovery, finalization, time, expression):
    time[0] += 1
    discovery[start_vertex] = time[0]
    expression.append(f"({start_vertex}")
    #usando de recursividade para implementação 
    for v in graph[start_vertex]:
        if discovery[v] == -1:
            dfs(graph, v, discovery, finalization, time, expression)

    time[0] += 1
    finalization[start_vertex] = time[0]
    expression.append(f"{start_vertex})")


def dfs_init(n, graph):

    discovery = [-1] * n
    finalization = [-1] * n
    time = [0]
    expression = []

    for vertex in range(n):
        if discovery[vertex] == -1:
            dfs(graph, vertex, discovery, finalization, time, expression)

    return ' '.join(expression)

#Função main

n, m = (int(tmp) for tmp in input().split(" "))
graph = adj = [[] for _ in range(n)]
for k in range(m):
    i, j = (int(tmp) for tmp in input().split(" "))
    adj[i].append(j)
dfs_parentheses_expression = dfs_init(n, graph)
print(dfs_parentheses_expression)