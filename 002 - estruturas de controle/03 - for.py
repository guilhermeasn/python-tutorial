# Escreva um programa para encontrar a soma S = 3 + 6 + 9 + .... + 333.
S = 0
for C in range(3, 334, 3): S += C
print('Soma de 3 + 6 + 9 + .... + 333:', S)

# Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número.
M = int(input('Tabuada de: '))
if M < 0: raise ValueError('Não é permitido números negativos')
for C in range(10) :
    N = C + 1
    print(M, 'x', N, '=', M * N)
