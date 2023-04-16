# Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6) 
# Refaça o exercício 1, identificando o conceito aprovado (média superior a 6), exame (média entre 4 e 6) ou reprovado (média inferior a 4).

try:
    n1 = float(input('Nota do teste: '))
    n2 = float(input('Nota da prova: '))
except ValueError as error:
    print('Nota inválida')
    exit()

m = (n1 + n2) / 2
print('Média:', m, ('👍', '👎')[m < 6])

if m >=6: print('APROVADO')
elif m < 4: print('REPROVADO')
else: print('RECUPERAÇÃO')

print(m > 6 and 'Parabéns!' or 'Estude mais!')
