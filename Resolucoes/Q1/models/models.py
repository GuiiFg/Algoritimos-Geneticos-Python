from itertools import count
import statistics
from Resolucoes.Q1.models.ListaEncadeada import ListaEncadiada

# O individuo carrega seu codigo genetico
class Individuo:
    
    def __init__(self, id:int, genes:list[str]) -> None:
        # o id identifica o individuo
        self.__id = id

        # Tranformas as letras em maiusculas caso nao sejam
        for i in range(len(genes)):
            genes[i] = genes[i].upper()

        # o genes armazenas as caracteristicas desse individuo
        self.__genes:list[str] = genes
        self.__pontuacao:int = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pontuacao(self) -> int:
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, value):
        self.__pontuacao = value

    @property
    def genes(self):
        return self.__genes

    @genes.setter
    def genes(self, value):
        self.__genes = value

class Populacao:
    
    def __init__(self, limite_individuos:int) -> None:
        
        # Armazena todos os individuos da população
        self.__individuos : list[Individuo] = []

        # Controla a população em quantidade
        self.__limite_individuos:int = limite_individuos

        # Armazena a pontuação media da população após a avaliação
        self.__pontuacao_media = None

        # Armazena o rinking dos individuos do melhor ao pior
        self.__ranking:list = []

        # controla o id de cada individo e a quantidade de individuos que ja passaram pela polulação
        self.__id_max = 0

    @property
    def ranking(self):
        return self.__ranking
    
    @property
    def limite_individuos(self):
        return self.__limite_individuos

    @property
    def pontuacao_media(self):
        return self.__pontuacao_media

    # Pega um gene e cria um novo individuo a partir deste gene
    def InserirIndividuo(self, genes:list[str]):
        novo_individuo = Individuo(self.__id_max +1, genes)
        self.__id_max += 1

        # Caso adiciar este novo individuo ultrapasse a quantidade max, ele não será adicionado
        if len(self.__individuos) < self.__limite_individuos:
            self.__individuos.append(novo_individuo)
        else:
            raise TypeError("Limite de individuos atingido")

    def RemoverIndividuo(self, id:int):
        removed:bool = False
        for individuo in self.__individuos:
            if individuo.id == id:
                self.__individuos.remove(individuo)
                removed = True

        if not removed:
            raise TypeError("Individuo não encontrado")

    def AcharIndividuos(self, ids:list) -> list[Individuo]:

        individuos = []

        for individuo in self.__individuos:
            if individuo.id in ids:
                individuos.append(individuo)

        return individuos

    def AvaliarPopulacao(self):

        self.__ranking = []
        pre_ranking = ListaEncadiada()
        notas:list[int]= []

        for individuo in self.__individuos:
            pontuacao = AvaliacaoIndividual(individuo)
            pre_ranking.InserirElemento(individuo.id, pontuacao)
            notas.append(pontuacao)

        self.__ranking = pre_ranking.GerarLista()
        self.__pontuacao_media = statistics.mean(notas)

# A avaliacao individual ira testa o gene do individuo e ver quantos pontos ele consegue em relação ao objetivo
def AvaliacaoIndividual(individuo:Individuo) -> int:

    grafo_mapa = {
        "A":{
            "A":125,
            "B":100,
            "C":125,
            "D":100,
            "E":75
        },
        "B":{
            "B":125,
            "A":100,
            "C":50,
            "D":75,
            "E":125
        },
        "C":{
            "C":125,
            "A":125,
            "B":50,
            "D":100,
            "E":125
        },
        "D":{
            "D":125,
            "A":100,
            "B":75,
            "C":100,
            "E":50
        },
        "E":{
            "E":125,
            "A":75,
            "B":125,
            "C":125,
            "D":50
        }
    }

    pontuacao = 0

    if not (
        "A" in individuo.genes
        and "B" in individuo.genes
        and "C" in individuo.genes
        and "D" in individuo.genes
        and "E" in individuo.genes):
        pontuacao += 250

    pontuacao += grafo_mapa[individuo.genes[0]][individuo.genes[1]]
    pontuacao += grafo_mapa[individuo.genes[1]][individuo.genes[2]]
    pontuacao += grafo_mapa[individuo.genes[2]][individuo.genes[3]]
    pontuacao += grafo_mapa[individuo.genes[3]][individuo.genes[4]]

    return pontuacao

def CruzamentoGenetico(pai:Individuo, mae:Individuo) -> list:

    filhos = []

    for i in range(2):
        if i == 0:
            caracteristicasFixos = pai.genes[2:4]
            caracteristicasAusentes = [x for x in pai.genes if x not in pai.genes[2:4]]

            ordem = []

            for carct in caracteristicasAusentes:
                contador = 0
                for x in mae.genes:
                    if x == carct:
                        ordem.append([x, contador])
                        break
                    else:
                        contador += 1
            
            print(ordem)
            
        else:
            pass

    return filhos

def MutacaoGenetica(individuo:Individuo) -> list:

    gene = individuo.genes
    aux = gene[1]
    gene[1] = gene[3]
    gene[3] = aux

    return gene

