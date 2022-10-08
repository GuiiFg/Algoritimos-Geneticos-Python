from .no import No

# Essa lista tem o objetivo de organizar o ranking dos individuos
# Desta forma ao inserir um elemento, ela já armazena o elemento na sua devida posição de acordo com
# a sua pontuação.
# No final, ela retorna uma lista com a ordem exata dos elementos e suas pontuações.

class ListaEncadiada:

    def __init__(self):
        self.__head__ = None

    def InserirElemento(self, id:int, pontuacao:int):

        novo_no:No = No(id, pontuacao)
        
        if self.__head__ == None:
            self.__head__ = novo_no
        else:
            aux = self.__head__

            while True:
                if novo_no.pontuacao >= aux.pontuacao:
                    if aux == self.__head__:
                        novo_no.prox = aux
                        aux.ante = novo_no
                        self.__head__ = novo_no

                    else:
                        aux2:No = aux.ante
                        novo_no.prox = aux
                        novo_no.ante = aux2
                        aux2.prox = novo_no
                    
                    break

                else:
                    if aux.prox != None:
                        aux = aux.prox

                    else:
                        novo_no.ante = aux
                        aux.prox = novo_no
                        break        
    
    def MostrarElementos(self):

        aux = self.__head__

        while aux != None:
            print(f"id: {aux.id} pontuacao: {aux.pontuacao}")
            aux = aux.prox

    def GerarLista(self) -> list:

        aux = self.__head__

        lista = []

        while aux != None:
            lista.append([aux.id, aux.pontuacao])
            aux = aux.prox

        return lista