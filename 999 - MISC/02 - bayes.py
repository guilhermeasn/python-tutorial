print('''
Numa certa região, a probabilidade de chuva em um dia qualquer de primavera é de 0,1.
Um meteorologista da TV acerta suas previsões em 80% dos dias em que chove e em 90% dos dias em que não chove.

a. Qual é a probabilidade do meteorologista acertar sua previsão?
b. Se houve acerto na previsão feita, qual a probabilidade de ter sido um dia de chuva?
''')

PDeChover = 0.1
PNaoChover = 0.9
PChoveEAcerta = 0.8
PNaoChoveEAcerta = 0.9

print('''
Lei da probabilidade total
P(A) = P(A|B1).P(B1) + P(A|B2).P(B2)
''')

PDeAcertar = PChoveEAcerta * PDeChover + PNaoChoveEAcerta * PNaoChover

print('A probabilidade do metereologista acertar sua previsao é de', round(PDeAcertar * 100, 2), '%')

print('''
Teorema de Bayes
P(A|B) = P(B|A).P(A)/P(B)
P(B|A) = P(A|B).P(B)/P(A)
''')

PDeAcertarEChover = PChoveEAcerta * PDeChover / PDeAcertar

print('A probabilidade de ter chovido é de', round(PDeAcertarEChover * 100, 2), '%')
