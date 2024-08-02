from random import randint

def gera_numeros() -> list:
    soma = randint(12, 40)
    n1 = randint(1, soma-5)
    n2 = soma-n1
    while True:
        n_errado = randint(3, soma-5)
        if n_errado+n1 != soma and n_errado+n2 != soma:
            break
    lista_num = [n1, n2, n_errado, soma]
    return lista_num

# n1, n2, n_errado, soma = gera_numeros()
# print(f"soma: {soma}, n errado:{n_errado}, {n1,n2}")