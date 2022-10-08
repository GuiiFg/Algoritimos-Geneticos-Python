

populacao = Populacao(10)

populacao.InserirIndividuo(["C","E","A","B","D"])
populacao.InserirIndividuo(["A","C","E","B","D"])
populacao.InserirIndividuo(["A","D","B","C","E"])
populacao.InserirIndividuo(["B","A","E","C","D"])
populacao.InserirIndividuo(["E","D","B","A","C"])

populacao.AvaliarPopulacao()
populacao.pontuacao_media
populacao.ranking

inds = populacao.AcharIndividuos([populacao.ranking[0][0],populacao.ranking[1][0],populacao.ranking[3][0]])

CruzamentoGenetico(inds[0],inds[1])
MutacaoGenetica(inds[2])