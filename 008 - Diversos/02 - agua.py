peso = float(input("Qual é seu peso em kg? ").replace(',', '.'))

min = peso * .035
max = peso * .05

smin = "{:.3f}".format(min).replace('.', ',')
smax = "{:.3f}".format(max).replace('.', ',')

print("\nConsmo de água recomendado entre %s e %s litros por dia.\n" % (smin, smax))
