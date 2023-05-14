from helper import getPorcent

print('''
Em uma prova de múltipla escolha, cada questão tem 5 alternativas, sendo apenas uma delas correta.
Ao não saber a resposta, o aluno “chuta” aleatoriamente uma resposta qualquer entre as possíveis
escolhas. Levando-se em conta um aluno mediano, que saiba 60% do conteúdo, qual será a chance
de ele acertar uma das 5 questões escolhida aleatoriamente? E qual a chance de ele acertar
exatamente 3 questões?
''')

PAcertarSemSaber = .2
PAcertarSabendo = 1

PSaber = .6
PNaoSaber = .4

print('''
Lei da probabilidade total
P(A) = P(A|B1).P(B1) + P(A|B2).P(B2) + P(A|B3).P(B3) + ...
''')

PAcertar = PAcertarSabendo * PSaber + PAcertarSemSaber * PNaoSaber

print('Chance dele acertar é de', getPorcent(PAcertar))
