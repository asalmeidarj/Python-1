""" Criando uma classe chamada livro """


class Livro:
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma ref. a cada atributo de um obj. criado a partir desta classe
    def __init__(self):  # Construtor
        self.titulo = "O monge e o Executivo"
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe")

    def imprime(self):  # Método recebe como parâmetro atributos do obj. criado
        print("Foi criado o livro %s e ISBN %d" % (self.titulo, self.isbn))


#########################################
#  Comandos para utilizar no terminal   #
# Criando uma instância da classe livro #
#         ipython -i classes01.py       #
#         Livro1 = Livro()              #
#         type(Livro1)                  #
#         Livro1.titulo                 #
#         Livro1.ISBN                   #
#         Livro1.imprime                #
#########################################
