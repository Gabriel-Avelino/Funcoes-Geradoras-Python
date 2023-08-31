from pympler.asizeof import asizesof


def dobro(lista):
    for i in lista:
        yield i * 2
    

x = dobro(range(0, 100))

while True:
    try:
        print(next(x))
    except StopIteration:
        break  

print()

for i in x:
    print(i)

