"""
Por padrão os maories valores sempre são colocados ao lado direito, 
então para encontrar o valor máximo basta apenas seguir os nós da
direita até encontrar o próximo valor nulo(folha da árvore)
"""

def tree_maximum(node):
    while node.right is not None:
        node = node.right
    return node