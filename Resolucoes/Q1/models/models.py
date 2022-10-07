import statistics

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
    def pontuacao(self):
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
        
        self.__individuos : list[Individuo] = []
        self.__limite_individuos:int = limite_individuos
        self.__pontuacao_media = 0
        self.__ranking:dict = {}

    @property
    def ranking(self):
        return self.__ranking
    
    @property
    def limite_individuos(self):
        return self.__limite_individuos

    @property
    def pontuacao_media(self):
        return self.__pontuacao_media

    def InserirIndividuo(self, individuo:Individuo):

        if len(self.__individuos) < self.__limite_individuos:
            self.__individuos.append(individuo)
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

    def AvaliarPopulacao(self):

        self.__ranking = {}
        notas:list[int]= []

        for individuo in self.__individuos:
            pontuacao = AvaliacaoIndividual(individuo)
            self.__ranking[individuo.id] = pontuacao
            notas.append(pontuacao)

        self.__pontuacao_media = statistics.mean(notas)

def AvaliacaoIndividual(individuo:Individuo) -> int:

    grafo_mapa = {
        "A":{
            "B":100,
            "C":125,
            "D":100,
            "E":75
        },
        "B":{
            "A":100,
            "C":50,
            "D":75,
            "E":125
        },
        "C":{
            "A":125,
            "B":50,
            "D":100,
            "E":125
        },
        "D":{
            "A":100,
            "B":75,
            "C":100,
            "E":50
        },
        "E":{
            "A":75,
            "B":125,
            "C":125,
            "D":50
        }
    }

    pontuacao = 0

    pontuacao += grafo_mapa[individuo.genes[0]][individuo.genes[1]]
    pontuacao += grafo_mapa[individuo.genes[1]][individuo.genes[2]]
    pontuacao += grafo_mapa[individuo.genes[2]][individuo.genes[3]]
    pontuacao += grafo_mapa[individuo.genes[3]][individuo.genes[4]]

    return pontuacao
    

populacao = Populacao(10)

populacao.InserirIndividuo(Individuo(1, ["C","E","A","B","D"]))
populacao.InserirIndividuo(Individuo(2, ["A","C","E","B","D"]))
populacao.InserirIndividuo(Individuo(3, ["A","D","B","C","E"]))
populacao.InserirIndividuo(Individuo(4, ["B","A","E","C","D"]))
populacao.InserirIndividuo(Individuo(5, ["E","D","B","A","C"]))

populacao.AvaliarPopulacao()
populacao.pontuacao_media
populacao.ranking