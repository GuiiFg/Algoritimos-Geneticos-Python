from Resolucoes.Q1.models.models import *
import time

# Cria uma nova populacao com o maximo de 5 individuos
populacao = Populacao(5)

# Insere os primeiro individuos na população
genes = [
    ["C","E","A","B","D"],
    ["A","C","E","B","D"],
    ["A","D","B","C","E"],
    ["B","A","E","C","D"],
    ["E","D","B","A","C"]
]
for gene in genes:
    populacao.InserirIndividuo(gene)

while True:
    populacao.AvaliarPopulacao()
    print("-----------------------")
    print(f"Ranking: {populacao.ranking}")
    print(f"Media: {populacao.pontuacao_media}")
    print(f"Aguardando 3s para nova geração...")
    time.sleep(3)

    

    novos_genes = []

    print("Selecionando melhores")
    # seleciona os melhores para cruzamento e mutação
    melhores_individuos = populacao.AcharIndividuos([populacao.ranking[0][0],populacao.ranking[1][0],populacao.ranking[3][0]])

    print("cruzando melhores")
    # Cruza os dois melhores
    filhos = CruzamentoGenetico(melhores_individuos[0],melhores_individuos[1])
    for filho in filhos:
        novos_genes.append(filho)

    print("mutando 1")
    # Muta o 3 melhor
    novos_genes.append(MutacaoGenetica(melhores_individuos[2]))

    print("selecioando os piores")
    # Seleciona os piores individuos
    piores_individuos = populacao.AcharIndividuos([populacao.ranking[-3][0],populacao.ranking[-2][0],populacao.ranking[-1][0]])

    print("excluindo os piores")
    # Exclui os 3 piores inidividuos
    for individuo in piores_individuos:
        populacao.RemoverIndividuo(individuo.id)

    print("Adicionando novos")
    # Adiciona os novos individuos
    for gene in novos_genes:
        populacao.InserirIndividuo(gene)

