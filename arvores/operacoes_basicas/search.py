def search(node, valor_referencia):
    """
    Busca recursiva em árvore binária.
    - caso base: nó é None (não encontrado) ou chave coincide com o valor buscado.
    - explora a subárvore esquerda se o valor procurado for menor que a chave atual.
    - explora a subárvore direita caso contrário.
    """
    if node == None or node.key == valor_referencia:
        return node #retorna valor de referência se encontrar correspondente, caso contrario retorna None
    if valor_referencia < node.key:
        return search(node.left,valor_referencia)
    return search(node.right,valor_referencia) #

def iterative_search(node, valor_referencia):
    """
    Na busca com recursividade a cada chamada recursiva é armazenado em memória(em uma estrutura de pilha)
    uma informação referente a função, até encontrar o caso base. Enquanto a maneira feita com o loop mexe apenas
    com a atualização dos ponteiros que referenciam a variável, sendo assim menos custosa em termos de 
    alocação de memória.
    """
    while node is not None and node.key != valor_referencia:
        if node.key < valor_referencia:
            node = node.left
        else:
            node = node.right
    return node #retorna valor esperado ou nulo

