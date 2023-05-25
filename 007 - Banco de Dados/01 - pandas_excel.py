import pandas
import os;


dir = os.path.dirname(os.path.realpath(__file__))
db = pandas.read_excel(dir + r"\Vendas - Dez.xlsx")

print(db['Quantidade'].sum())
