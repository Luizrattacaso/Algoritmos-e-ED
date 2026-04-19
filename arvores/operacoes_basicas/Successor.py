from  Classes import Tree
from arvores.operacoes_basicas.tree_minimum import tree_minimum

def Successor(node=Tree.root):
    if node.right is not None: # ------> Se não for folha e tiver filho direito
        return tree_minimum(node.right) # ------> Procure o menor valor dentre os números maiores que o node

    father = node.father

    while father is not None and node == father.right: # ------> se não for root e se o node for filho esquedo de um pai, retorne o pai
        node = father
        father = father.father
    return father # se não retorne o avó e assim por diante