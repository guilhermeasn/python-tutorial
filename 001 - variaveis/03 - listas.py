# Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
L = [5, 7, 2, 9, 4, 1, 3]
print('Lista: ', L)

# a) tamanho da lista
print('Tamanho da lista: ', len(L))

# b) maior valor da lista.
print('Maior valor da lista: ', max(L))

# c) menor valor da lista.
print('Menor valor da lista: ', min(L))

# d) soma de todos os elementos da lista.
print('Soma os valores da lista: ', sum(L))

# e) lista em ordem crescente.
L.sort()
print('Lista ordenada crescente: ', L)

# f) lista em ordem decrescente.
L.reverse()
print('Lista ordenada decrescente: ', L)

#Gere uma lista de contendo os múltiplos de 3 entre 1 e 50.
R = list(range(1, 50, 3))
print('\nLista entre 1 e 50, de 3 em 3:\n', R)
