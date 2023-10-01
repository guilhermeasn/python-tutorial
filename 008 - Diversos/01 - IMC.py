altura = int(input('Qual a sua altura em centímetros? '))
metro2 = (altura / 100) ** 2

tabela = {
    'ideal': 18.5 * metro2,
    'sobre':   25 * metro2,
    'grau1':   30 * metro2,
    'grau2':   35 * metro2,
    'grau3':   40 * metro2
}

print("\n")
print("Abaixo do peso: menos que %.0f kg" % tabela['ideal'])
print("PESO IDEAL: entre %.0f kg e %.0f kg" % (tabela['ideal'], tabela['sobre']))
print("Sobrepeso moderado: entre %.0f kg e %.0f kg" % (tabela['sobre'], tabela['grau1']))
print("Obesidade (grau I): entre %.0f kg e %.0f kg" % (tabela['grau1'], tabela['grau2']))
print("Obesidade severa (grau II): entre %.0f kg e %.0f kg" % (tabela['grau2'], tabela['grau3']))
print("Obesidade morbida (grau III): maior que %.0f kg" % tabela['grau3'])
print("\n")
