# Crie uma função para desenhar uma linha, usando o  caractere  '_'. O tamanho da linha deve ser definido na chamada da função.

def line(size: int) -> str:
    strg = ''
    while(size > 0):
        size -= 1
        strg += '_'
    return strg

print(line(int(input('Tamanho da linha: '))))

# Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os.

def listar(lista: list):
    count = 0
    for item in lista:
        count += 1
        print(count, item)

print()
listar(['a', 'b', 'c', 'd', 'e'])