""" Implementação de Árvore Binária """


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):  # percurso em ordem simétrica
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end= '')
        if node.right:
            self.simetric_traversal(node.right)            
            print('(', end='')

    def postorder_travesal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_travesal(node.left)
        if node.right:
            self.postorder_travesal(node.right)
        print(node)

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node('20')
    n2 = Node('11')
    n3 = Node('25')
    n4 = Node('14')
    n5 = Node('12')
    n6 = Node('13')
    n7 = Node('16')
    n8 = Node('9')
    n9 = Node('8')
    n0 = Node('2')


    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n5.left = n8
    n8.right = n7


    tree.root = n0
    return tree


if __name__ == "__main__":
    tree = postorder_example_tree()
    print("Percurso em pós ordem:")
    tree.postorder_travesal()

