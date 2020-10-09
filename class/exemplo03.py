""" Classe para criar pilha """


class Pilha:
    def __init__(self):  # Inicializador da classe
        self.__stack = []
        print('Inicializador foi instanciado')

    def adicionar(self, elemento):  # adicionar elemento a pilha
        self.__stack.append(elemento)
        print(f'{elemento} foi adicionado ao final da pilha')

    def remover(self):  # remover ultimo elemento adicionado
        return self.__stack.pop()
        print(f'{self.elemento}')

    def mostrar(self):
        print(f'Pilha: {self.__stack}')  # mostra os elementoes adicionados


##########################################
#  Criando uma instância da classe Fila  #
#  *Comandos para utilizar no terminal*  #
#         ipython -i exemplo03.py        #
#         livro = Pilha()                #
#         type(livro)                    #
#         livro.adicionar('O Estudante') #
#         livro.adicionar('O matemático')#
#         livro.mostrar                  #
#         livro.adicionar(2020)          #
#         livro.remover ( )              #
#         livro.mostrar                  #
#         livro.remover ( )              #
#         livro.mostrar                  #
##########################################
