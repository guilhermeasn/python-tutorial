class animal:
    def __init__(self, nome) -> None:
        self.nome = nome.title()
    def __str__(self) -> str:
        return self.nome + ' disse ' + self.som()
    def som(self) -> str:
        pass

class cachorro(animal):
    def som(self) -> str:
        return 'au-au'
    
class gato(animal):
    def som(self) -> str:
        return 'miau'
    
class galo(animal):
    def som(self) -> str:
        return 'cocorico'

def main():
    print("Escolha um animal:", "\n1 - Cachorro", "\n2 - Gato", "\n3 - Galo")
    escolha = int(input('Digite o número correnpondente: '))
    if escolha == 1: print(cachorro(input('Nome do cachorro: ')))
    elif escolha == 2: print(gato(input('Nome do gato: ')))
    elif escolha == 3: print(galo(input('Nome do galo: ')))
    else: raise ValueError('Nenhum animal selecionado')

if __name__ == "__main__": main()
