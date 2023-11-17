from collections import deque

def bfs(n, m, edges):
    adj = [[] for _ in range(n)]
    
    for i, j in edges:
        adj[i].append(j)

    matriz_distancias = [[-1] * n for _ in range(n)]

    for s in range(n):
        d = [-1] * n
        cor = [0] * n
        INF = 999999
        BRANCO = 1
        CINZA = 2
        PRETO = 3
        d[s] = 0

        Q = deque([s])

        while Q:
            u = Q.popleft()
            for v in adj[u]:
                if cor[v] == 0:
                    d[v] = d[u] + 1
                    cor[v] = CINZA
                    Q.append(v)
            cor[u] = PRETO

        matriz_distancias[s] = d

#formatando a saída
    for i in range(n):
        print(f"{i}: {' '.join(map(str, matriz_distancias[i]))}")

#Função Main
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

bfs(n, m, edges)
