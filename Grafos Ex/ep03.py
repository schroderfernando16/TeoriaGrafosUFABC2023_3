def dfs(n, m, edges):
    adj = [[] for _ in range(n)]
    
    for i, j in edges:
        adj[i].append(j)

    tempo = 1
    descoberta = [-1] * n
    finalizacao = [-1] * n

#Trabalha com o tempo de visita usando nonlocal 
    def visita(v):
        nonlocal tempo
        descoberta[v] = tempo
        tempo += 1
        for u in adj[v]:
            if descoberta[u] == -1:
                visita(u)
        finalizacao[v] = tempo
        tempo += 1

    for v in range(n):
        if descoberta[v] == -1:
            visita(v)

    return descoberta, finalizacao

# Entrada
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# DFS
descoberta, finalizacao = dfs(n, m, edges)

print(descoberta)
print(finalizacao)
