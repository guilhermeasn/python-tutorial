#Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (𝑥² + 𝑦²) / (𝑥−𝑦)²
X = float(input("Número X: "))
Y = float(input("Número Y: "))
try:
    Z = (X**2 + Y**2) / (X-Y)**2
    print("Resultado: ", Z)
except:
    print('Impossível calcular')

#Escreva  um  programa  que  receba  o  salário  de  um  funcionário  (float),  e  retorne  o  resultado  do novo salário com reajuste de 35%
S = float(input("\nSalário atual: "))
print('Salário ajustado: %.2f' %(S + (S*.35)))
