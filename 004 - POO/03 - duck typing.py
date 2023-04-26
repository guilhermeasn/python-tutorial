class cachorro():
    def who(self) -> str:
        return 'sou um cachorro'
    
class gato():
    def who(self) -> str:
        return 'sou um gato'
    
class galo():
    def who(self) -> str:
        return 'sou um galo'
    
who = lambda animal : animal.who()

def main():
    print("Escolha um animal:", "\n1 - Cachorro", "\n2 - Gato", "\n3 - Galo")
    escolha = int(input('Digite o número correnpondente: '))
    if escolha == 1: print(who(cachorro()))
    elif escolha == 2: print(who(gato()))
    elif escolha == 3: print(who(galo()))
    else: raise ValueError('Nenhum animal selecionado')

if __name__ == "__main__": main()
