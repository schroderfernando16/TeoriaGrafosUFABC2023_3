#Fernando Schroder Rodrigues RA: 11201921885

#Usando POO para impelemntar de forma mais limpa e otimizada a código, foi cirada uma classe de prioridade.
class PriorityQueue:
    def __init__(self, n, keys):
        self.queue = [0] * n
        self.keys = keys
    #verifica se os valores são vazio)
    def is_empty(self):
        return all(q == 0 for q in self.queue)

    #Insere um nó na fila
    def insert(self, i):
        self.queue[i] = 1

    #Algortimo de busca na fila
    def search(self, i):
        return self.queue[i]
    #Aqui é pego o minimo dentro do números
    def extract_min(self):
        min_index = -1
        min_key = float('inf')
        for i, q in enumerate(self.queue):
            if q == 1 and self.keys[i] < min_key:
                min_key = self.keys[i]
                min_index = i
        if min_index != -1:
            self.queue[min_index] = 0
        return min_index

    def min(self):
        min_index = -1
        min_key = float('inf')
        for i, q in enumerate(self.queue):
            if q == 1 and self.keys[i] < min_key:
                min_key = self.keys[i]
                min_index = i
        return min_index

    def __str__(self):
        return str(self.queue)


n, k = map(int, input().split())
keys = list(map(int, input().split()))
q = PriorityQueue(n, keys)

for _ in range(k):
    operation = input().split()
    op_type = operation[0]

    if op_type == 'I':  # Insert
        q.insert(int(operation[1]))
        print(q)
    elif op_type == 'M':  # Min
        print(q.min(), q)
    elif op_type == 'E':  # Extract Min
        print(q.extract_min(), q)
    elif op_type == 'B':  # Search
        print(q.search(int(operation[1])), q)
    elif op_type == 'V':  # Is Empty
        print(q.is_empty(), q)
