from random import randint

def gera_numeros() -> list:
    n1 = randint(1, 99)
    n2 = randint(1, 99)
    n3 = randint(1, 99)
    n4 = randint(1, 99)
    lista_num = [n1, n2, n3, n4]
    return lista_num

print(gera_numeros())