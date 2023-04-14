#Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (𝑥² + 𝑦²) / (𝑥−𝑦)²
X = int(input("Número X: "))
Y = int(input("Número Y: "))
Z = (X**2 + Y**2) / (X-Y)**2
print("Resultado: ", Z, "\n\n")

#Escreva  um  programa  que  receba  o  salário  de  um  funcionário  (float),  e  retorne  o  resultado  do novo salário com reajuste de 35%
S = float(input("Salário atual: "))
print('Salário ajustado: ', S + (S*.35))