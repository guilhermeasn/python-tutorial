# Escreva um programa que leia 10 notas e informe a média dos alunos

notas = []

while(len(notas) < 10):
    notas.append(float(input('Nota: ')))

print('Notas:', notas)
print('Média:', sum(notas) / len(notas))
