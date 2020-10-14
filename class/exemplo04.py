""" Classe Deque """ 


class Deque:
    def __init__(self):
        self.deque = []  # inicia com deque vazio
        self.len = 0  # ler o tamanho do deque
        print("Chamando inicializador da classe")

    def inserir_esquerda(self, elemento):  
        self.deque.insert(0, elemento)  # inserir elemento no início do deque
        self.len += 1
        print(f' sua lista possui um novo elemento ao lado esquerdo {self.deque}')

    def remover_esquerda(self):  
        self.deque.pop(0)   # remove elemento no início do deque 
        self.len -= 1
        print(f' seu deque agora tem esses elementos {self.deque} ')

    
    def inserir_direita(self, elemento):  
        self.deque.insert(self.len, elemento)  # inserir elemento ao final do deque
        self.len += 1
        print(f' sua lista possui um novo elemento {self.deque} ao lado direiro.')

    def remover_direita(self):  
        self.deque.pop(self.len - 1)  #remover no final 
        self.len -= 1
        print(f' seu deque agora tem esses elementos {self.deque} ')

    def exibir(self):  # verifica se existe elementos no deque
        if self.len == 0:
            return "seu deque não possui elementos"
        return f" seu deque atual é {self.deque}"


#########################################
# Criando uma instância da classe Deque #
#  *Comandos para utilizar no terminal* #
#         ipython -i classes04.py       #
#         deque = Deque()               #
#         type(deque)                   #
#         deque.exibir()                #
#  deque.inserir_esquerda('Daniel')     #
#  deque.inserir_direita('Alessandro')  #
#  deque.inserir_esquerda('Miguel')     #
#     deque.inserir_direita(2020)       #
#         deque.exibir()                #
#       deque.remover_esquerda()        #
#       deque.remover_direita()         #
#       deque.remover_esquerda()        #
#       deque.remover_direita()         #
#            deque.exibir()             #
#########################################
