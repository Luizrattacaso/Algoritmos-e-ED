"""
Por padrão os menores valores sempre são colocados ao lado esquedo, 
então para encontrar o valor mínimo basta apenas seguir os nós da
esquerda até encontrar o próximo valor nulo(folha da árvore)
"""

def tree_minimum(node):
    while node.left is not None:
        node = node.left
    return node