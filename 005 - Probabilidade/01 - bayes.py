from helper import getPorcent

print('''
Um piloto de fórmula um tem 50% de probabilidade de vencer determinada corrida, quando esta se realiza sob chuva.
Caso não chova durante a corrida, sua probabilidade de vitória é de 25%.
Se o serviço de meteorologia estima em 30% a probabilidade de que chova durante a corrida.

1) qual é a probabilidade desse piloto ganhar?
2) sabendo que o piloto venceu, qual a probabilidade de ter chovido durante a competição?
''')

PVencerComChuva = 0.5
PVencerSemChuva = 0.25
PDeChover = 0.3
PNaoChover = 0.7

print('''
Lei da probabilidade total
P(A) = P(A|B1).P(B1) + P(A|B2).P(B2)
''')

PDeVencer = PVencerComChuva * PDeChover + PVencerSemChuva * PNaoChover

print('A probabilidade do piloto vencer é de', getPorcent(PDeVencer))

print('''
Teorema de Bayes
P(A|B) = P(B|A).P(A)/P(B)
P(B|A) = P(A|B).P(B)/P(A)
''')

PDeVencerEChover = PVencerComChuva * PDeChover / PDeVencer

print('A probabilidade do piloto vencer é de', getPorcent(PDeVencerEChover))
