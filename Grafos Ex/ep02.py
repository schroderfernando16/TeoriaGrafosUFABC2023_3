# Assume que Q eh uma lista
def insere (Q, x):
  Q.append (x)

# Assume que Q nao eh vazio
def remove (Q):
  return Q.pop (0)

def vazio (Q):
  return len (Q) == 0


n, m, s = (int(tmp) for tmp in input().split(" "))

# lista adjacência
adj = [[] for _ in range(n)]

# le e atualiza lista
for k in range(m):
  i, j = (int(tmp) for tmp in input().split(" "))
  adj[i].append(j)

# algoritmo BFS

# inicializacao
# armazena as distâncias dos vértices
d = [0] * n
# armazena a cor de cada vertice
cor = [0] * n
# distancia infinita (vertice ainda nao processado)
INF = 999999
BRANCO = 1
CINZA = 2
PRETO = 3

# todos os vertices sao brancos e dist inf
for v in range (n):
  d[v] = INF
  cor[v] = BRANCO
d[s] = 0

# fila Q com vertice inicial
Q = [s]

# enquanto Q nao vazio o processamento continua
while not vazio (Q):
  # removendo o primeiro da fila
  u = remove (Q)
  # para cada vertice adjacente a u
  for v in adj[u]:
    # caso ainda nao tenha sido visitado
    if cor[v] == BRANCO:
      # atualiza distancia 
      d[v] = d[u] + 1
      # cinza pois ainda nao foi totalmente processado
      cor[v] = CINZA
      insere (Q, v)
  # foi totalmente processado muda para preto
  cor[u] = PRETO

print(f'1: {" ".join([str(i) for i in d])}')
