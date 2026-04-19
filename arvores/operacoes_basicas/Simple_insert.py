def insert_node(Tree, new_node):
    """
    insere um novo node na árvore binária.
    pré-requisito: new_node já deve ter os atributos 'left' e 'right' inicializados como None.
    """
    parent_node = None      # pai/refenrência do node. Começa sendo como o pai da raíz 
    current_node = Tree.root # ponteiro para percorrer a árvore a partir da raiz

    # percorre a árvore até encontrar uma posição vazia (None)
    while current_node is not None:
        parent_node = current_node  # atualiza o pai candidato antes de descer um nível
        
        # decide o caminho conforme a propriedade de ordenação dos valores de cada node
        if new_node.key < current_node.key:
            current_node = current_node.left
        else:
            current_node = current_node.right
    
    new_node.father = parent_node # insere vinculo com o pai(folha atual)
    
    # se a árvore estava vazia, o novo nó se torna a raiz
    if parent_node is None:
        Tree.root = new_node
    # caso contrário, insere como filho esquerdo ou direito do pai encontrado
    elif new_node.key < parent_node.key:
        parent_node.left = new_node
    else:
        parent_node.right = new_node