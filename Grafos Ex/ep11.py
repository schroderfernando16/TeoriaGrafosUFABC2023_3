#Fernando Schroder RA:11201921885

#Código de Floyd, retirado parte do stack overflow
def floyd_warshall(vertices, edges):
    INF = float('inf')
    dist = [[INF for _ in range(vertices)] for _ in range(vertices)]
    pi = [[-1 for _ in range(vertices)] for _ in range(vertices)]

    for i in range(vertices):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        pi[u][v] = u

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pi[i][j] = pi[k][j]

    return dist, pi

#função main com a formatacao para adequação do exercício
n, m = map(int, input("").split())
edges = []

print("")
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

distances, paths = floyd_warshall(n, edges)
print("[", end="")
aux =0
for row in distances:
    if aux<len(distances) -1:
        print(row)
    else: 
        print(row,end="")
        print("]")
    aux = aux+1
print("[", end="")
aux = 0
for row in paths:  
    
    if aux<len(paths)-1:
        print(row)
    else: 
        print(row,end="")
        print("]")

    aux = aux + 1

