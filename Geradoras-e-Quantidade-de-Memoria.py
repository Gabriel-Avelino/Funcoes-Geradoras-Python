# Dependendo do tamanho do valor, é necessária uma quantidade de memória diferente:

from pympler.asizeof import asizesof 

print(asizesof(1))  # 32 bits
print(asizesof(5000000000000000000000000000000000000000))   # 48 bits
print(asizesof('s'))  # 56 bits
print(asizesof('saguguigiugiygiugiuguyiugiugiugiuygiuyiuyhiuyhiuyhiuhy'))   # 104 bits
print(asizesof([1]))  # 96 bits: 32 para o número e 64 para a lista
print(asizesof([1, 2]))  # 136 bits: 56 para a lista e 40 para cada número
print(asizesof([1, 2, 3]))  # 176 bits: 56 para a lista e 40 para cada número
print(asizesof([1, 2, 3, 4]))  # 216 bits: 56 para a lista e 40 para cada número


def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i * 2)

    return lista_dobro


x = asizesof(dobro(range(0, 1000)))

print(x)  # 40856 bits