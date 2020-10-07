""" Criando uma classe chamada livro """


class Livro:
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma ref. a cada atributo de um obj. criado a partir desta classe
    def __init__(self):  # Inicializador
        self.titulo = "O monge e o Executivo"
        self.isbn = 9988888
        print("Inicializador chamado para criar um objeto desta classe")

    def imprime(self):  # Método recebe como parâmetro atributos do obj. criado
        print("Foi criado o livro %s e ISBN %d" % (self.titulo, self.isbn))


#########################################
# Criando uma instância da classe livro #
#  *Comandos para utilizar no terminal* #
#         ipython -i classes01.py       #
#         Livro1 = Livro()              #
#         type(Livro1)                  #
#         Livro1.titulo                 #
#         Livro1.isbn                   #
#         Livro1.imprime                #
#########################################
