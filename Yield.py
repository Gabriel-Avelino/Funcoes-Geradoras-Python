# O generator gasta menos memória:

from pympler.asizeof import asizesof 


def sequencia():
    # Return  # type = int
    i = 0
    while True:
        i = i + 1
        yield i # type = generator
    

x = sequencia()

print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4
print(next(x))  # 5
print(next(x))  # 6
print(next(x))  # 7
print(next(x))  # 8
print(next(x))  # 9
print(next(x))  # 10
print()

def dobro(lista):
    for i in lista:
        yield i * 2
    

x = dobro(range(0, 10000))
print(next(x))  # 2
print(next(x))  # 4
print(next(x))  # 6
print(next(x))  # 8
print(next(x))  # 10
print(asizesof(x))  # 584 bits


def dobro2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i)
    return lista_2


y = dobro2(range(0, 10000))
print(asizesof(y))  # 405176 bits