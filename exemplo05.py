""" Lista encadeada """


# Representação da classe nó
class Node:
    def __init__(self, data):  # inicializador
        self.data = data  # data representa os dados
        self.next = None  # local que armazena o próximo nó


class LinkedList:
    def __init__(self):  # inicializador vazio
        self.head = None  # a cabeça da lista encadeada

    def append(self, data):  # função para inserir elementos na lista vazia
        new_node = Node(data)  # nova variável de um nó atual
        if self.head == None:  # quando a lista esta vazia
            self.head = new_node
            return  # se a lista estiver vazia, iremos adicionar um novo nó

        current_node = self.head

        while current_node.next:  # função de percorrer toda estrutura de dados
            current_node = (
                current_node.next
            )  # pegando cada nó atual e passando para o próximo
        current_node.next = new_node  # no final quando a condição for falsa
        return

    def length(self):  # função que calcula o comprimento
        if self.head is None:  # verificar se o head é vazio
            return 0
        current_node = self.head
        total = 0  # Init count
        # Loop while end of linked list is not reached
        while current_node:  # enquanto ele for verdadeiro
            total += 1  # incrementa nosso contador
            current_node = current_node.next  # pula para o proximo nó
        return total

    def to_list(self):  # converte a lista encadeada de volta para lista normal
        node_data = []  # iniciar como um vetor vazio
        current_node = self.head  # igualar o nó atual com o head

        # estou pegando a lista encadeada e jogando para o array
        while current_node:
            node_data.append(current_node.data)  # salvar o valor do dado atual
            current_node = current_node.next
        return node_data

    # retorna o valor do nó em um index
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        current_idx = 0
        current_node = self.head
        while current_node != None:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1

    # reverse a linked list
    def reverse_linkedlist(self):  # inverter as setas da estrutura
        previous_node = None  # setar como vazio
        current_node = self.head  # nó atual

        # enquanto percorre a lista ele inverte os passos do nó
        while current_node != None:
            next = current_node.next  # próximo nó atual
            current_node.next = previous_node  # nó atual e atribuir ao nó anterior
            previous_node = current_node  # pegar anterior e colocar nó atual
            current_node = next  # pegar o nó atual e igualar ao next
        self.head = previous_node  # head sendo o nó anterior

    # precurar um elemento semelhante ou percorrer uma lista vinculada
    def search_item(self, value):
        if self.head == None:
            print("List has no elements")
            return
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                print("Item found")
                return True
            current_node = current_node.next
        print("Item not found")
        return False

    def display(self):  # mostra os elementos da lista encadeada
        contents = self.head
        # If the list is null
        if contents is None:  # se o conteúdo for nulo a lista não tem elemento
            print("List has no element")
        while contents:  # percorrer a lista e printar abaixo
            print(contents.data)
            contents = contents.next
        print("----------")  # print para separar

    # excluir um elemento ou um item no início
    def remove_at_start(self):
        if self.head == None:
            print("The list has no element to delete")
            return
        self.head = self.head.next

    # excluir um elemento ou item no final
    def remove_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None

    # Remover um nó com valor específico
    def remove_element_by_value(self, value):
        # Store head node
        current_node = self.head

        # If head node itself holds the value to be deleted
        if current_node != None:
            if current_node.data == value:
                self.head = current_node.next
                current_node = None
                return

        # Search for the value to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while current_node != None:
            if current_node.data == value:
                break
            prev = current_node
            current_node = current_node.next

        # if value was not present in linked list
        if current_node == None:
            return

        # Unlink the node from linked list
        prev.next = current_node.next
        current_node = None

    # Insert an item in a single linked list
    # add an item at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert an item in a single linked list
    # add an item at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # Insert an item in a single linked list
    # add an item at any index of the list
    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        current_node = self.head
        while i < index - 1 and current_node is not None:
            current_node = current_node.next
            i = i + 1
        if current_node is None:
            print("ERROR: Index out of range!")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node


# Test
listaEncadeada = LinkedList()
listaEncadeada.display()
# Add the elements
listaEncadeada.append(9)
listaEncadeada.append(3)
listaEncadeada.append(8)
listaEncadeada.append(2)

listaEncadeada.display()

print("The total number of elements are: " + str(listaEncadeada.length()))
print(listaEncadeada.to_list())  # Python list
print("---------")
listaEncadeada.reverse_linkedlist()  # Reverse linked list
listaEncadeada.display()

listaEncadeada.search_item(9)
listaEncadeada.search_item(99)

listaEncadeada.remove_at_start()
listaEncadeada.display()

listaEncadeada.remove_at_end()
listaEncadeada.display()

listaEncadeada.insert_at_start(1)
listaEncadeada.display()

listaEncadeada.insert_at_end(3)
listaEncadeada.display()

listaEncadeada.remove_element_by_value(3)
listaEncadeada.display()

listaEncadeada.insert_at_index(2, 88)
listaEncadeada.display()
