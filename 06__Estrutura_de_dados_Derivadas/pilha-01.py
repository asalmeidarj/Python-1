""" Pilha de itens """


def pilha():
    pilha = [2, 4, 6, 8]
    pilha.append(10)  # append adiciona elemento acima da pilha
    pilha.append(20)
    pilha.append(40)
    pilha.append(80)
    pilha.append(160)
    pilha.append(320)

    print(pilha)
    pilha.pop()  # pop remove o último elemento adicionado na pilha
    print(pilha)
    pilha.pop()
    print(pilha)


pilha()
