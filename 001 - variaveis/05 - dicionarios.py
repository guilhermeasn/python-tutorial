#  crie um dicionário de produtos de lanchonete
D = {
    "Salgado": 4.5,
    "Lanche": 6.5,
    "Suco": 3.0,
    "Refrigerante": 3.5,
    "Doce": 1.0
}
print("Cardápio: ", D)

#Considere um dicionário com 5 nomes de alunos e suas notas. Escreva um programa que calcule a média dessas notas. 
A = {
    "Antonio": 6,
    "Jose": 9,
    "Marcos": 3,
    "Maria": 8,
    "Joana": 10
}
print("Notas: ", A)
print("Mádia: ", sum(A.values()) / len(A))
