from random import randint

def gera_numeros() -> list:
    soma = randint(15, 45)
    n1 = randint(1, soma-5)
    n2 = soma-n1
    while True:
        n_errado = randint(3, soma-5)
        if n_errado+n1 != soma and n_errado+n2 != soma:
            break
    return [n1, n2, n_errado, soma]