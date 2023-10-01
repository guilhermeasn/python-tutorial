altura = int(input('Qual a sua altura em centímetros? '))
metro2 = (altura / 100) ** 2

tabela = {
    'baixo': 18.5 * metro2,
    'ideal':   25 * metro2,
    'acima':   30 * metro2,
    'grau1':   35 * metro2,
    'grau2':   40 * metro2
}

print("\n")
print("Abaixo do peso: menos que %.0f kg" % tabela['baixo'])
print("PESO IDEAL: entre %.0f kg e %.0f kg" % (tabela['baixo'], tabela['ideal']))
print("Sobrepeso moderado: entre %.0f kg e %.0f kg" % (tabela['ideal'], tabela['acima']))
print("Obesidade (grau I): entre %.0f kg e %.0f kg" % (tabela['acima'], tabela['grau1']))
print("Obesidade severa (grau II): entre %.0f kg e %.0f kg" % (tabela['grau1'], tabela['grau2']))
print("Obesidade morbida (grau III): maior que %.0f kg" % tabela['grau2'])
print("\n")
