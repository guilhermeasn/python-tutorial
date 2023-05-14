from helper import getPorcent

print('''
Um velejador experiente tem 50% de chance de vencer uma regata sob vento forte
Porém sem vento forte a possibilidade de vercer cai para 25%
Os serviços de metereologia estimam uma chance de ter vento forte em 30%

Qual a probabilidade do velejador vencer a competição?
''')

PVencerComVento = .5
PVencerSemVento = .25
PComVento = .3
PSemVento = .7

print('''
Lei da probabilidade total
P(A) = P(A|B1).P(B1) + P(A|B2).P(B2) + P(A|B3).P(B3) + ...
''')

PVencer = PVencerComVento * PComVento + PVencerSemVento * PSemVento

print('A chance de vencer é de', getPorcent(PVencer))
