from  Classes import Tree
from arvores.operacoes_basicas.tree_maximum import tree_maximum

def Predecessor(node=Tree.root):
    if node.right is not None: # ------> Se não for folha e tiver filho esquerdo
        return tree_maximum(node.left) # ------> Procure o maior valor dentre os números menores que o node

    father = node.father

    while father is not None and node == father.left: # ------> se não for root e se o node for filho direito de um pai, retorne o pai
        node = father
        father = father.father
    return father # se não retorne o avó e assim por diante