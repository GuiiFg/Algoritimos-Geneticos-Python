
class No:

    def __init__(self, id, pontuacao, prox = None, ante = None):
        self.__prox = prox
        self.__ante = ante
        self.__id = id
        self.__pontuacao = pontuacao
    
    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, value):
        self.__prox = value

    @property
    def ante(self):
        return self.__ante

    @ante.setter
    def ante(self, value):
        self.__ante = value

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
        
