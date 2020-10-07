""" Classe de criação de fila"""


class Fila:
    def __init__(self):  # Método inicializador
        self.fila = []
        print("Inicializador chamado para criar um objeto desta classe")

    def entrar(self, nome):  # Função que informa quem entra na fila.
        self.fila.append(nome)  # Utilizado para adicionar nomes na fila.
        print(f"{nome} entrou na fila")

    def sair(self):  # Função que informa quem sai da fila.
        # Utilizado para retirar nomes da fila em ordem de entrada e exibir
        print(f"{self.fila.pop(0)} saiu da fila")


#########################################
# Criando uma instância da classe Fila  #
#  *Comandos para utilizar no terminal* #
#         ipython -i exemplo02.py       #
#         Banco = Fila()                #
#         type(Banco)                   #
#         Banco.entrar('Daniel')        #
#         Banco.entrar('Alessandro')    #
#         Banco.fila                    #
#         Banco.sair ( )                #
#         Banco.fila                    #
#         Banco.sair ( )                #
#         Banco.fila                    #
#########################################
