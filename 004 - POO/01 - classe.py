class filme:
    def __init__(self, nome : str, ano : int, duracao : int) -> None:
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
    def __str__(self) -> str:
        return self.nome + ' - ' + str(self.ano) + ' - ' + str(self.duracao) + ' min'

filmeObj = filme(
    input('Nome do filme: '),
    int(input('Ano do filme: ')),
    int(input('Duração do filme: '))
)

print(filmeObj)
