import random

def gerar_populacao(tamanho_populacao, tamanho_individuo):
    return [[random.randint(0, 1) for _ in range(tamanho_individuo)] for _ in range(tamanho_populacao)]

populacao = gerar_populacao(100, 10)  # 100 indivíduos com 10 genes cada

print("populacao", populacao)

def avaliar(individuo):
    # Exemplo simples: somar os valores dos genes
    return sum(individuo)

aptidoes = [avaliar(ind) for ind in populacao]

print("aptidoes", aptidoes)

def selecionar_pais(populacao, aptidoes):
    total_aptidao = sum(aptidoes)
    selecao = random.choices(populacao, weights=aptidoes, k=len(populacao))
    return selecao

pais = selecionar_pais(populacao, aptidoes)

print("pais", pais)

def cruzar(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao(individuo, taxa_mutacao=0.01):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 if individuo[i] == 0 else 0
    return individuo

def gerar_nova_geracao(pais, taxa_mutacao):
    nova_geracao = []
    for i in range(0, len(pais), 2):
        pai1, pai2 = pais[i], pais[i + 1]
        filho1, filho2 = cruzar(pai1, pai2)
        nova_geracao.append(mutacao(filho1, taxa_mutacao))
        nova_geracao.append(mutacao(filho2, taxa_mutacao))
    return nova_geracao

for g in range(10) :
    nova_populacao = gerar_nova_geracao(pais, 0.01)
    print("geracao", g + 1, nova_populacao)