#Fernando Schroder RA:11201921885

#Usando POO para uma programação mais clara e código limpo
class Disjuntos:
    def __init__(self):
        self.set = []

#Insere o elemento
    def make_set(self, x):
        self.set.append([x])
#busca o elemento e retorna o indice dele
    def find_set(self, x):
        for i, subset in enumerate(self.set):
            if x in subset:
                return i
        return None
#Une os conjuntos
    def union(self, x, y):
        index_x = self.find_set(x)
        index_y = self.find_set(y)
        if index_x is not None and index_y is not None and index_x != index_y:
            self.set[index_x].extend(self.set[index_y])
            self.set[index_y] = []

    def __str__(self):
        return str(self.set)


n = int(input())
ds = Disjuntos()

for _ in range(n):
    operation = input().split()
    op_type = operation[0]
    x = operation[1]
#condicional para as operações
    if op_type == 'M': 
        ds.make_set(x)
        print(ds)
    elif op_type == 'F':  
        print(ds.find_set(x), ds)
    elif op_type == 'U': 
        y = operation[2]
        ds.union(x, y)
        print(ds)
