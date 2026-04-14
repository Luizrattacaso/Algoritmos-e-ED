from Classes import Tree, Node
from operacoes_basicas.search import search, iterative_search
from operacoes_basicas.insert import insert_node

t = Tree()

t.root = Node(10)

insert_node(t, Node(5))
insert_node(t, Node(15))

# busca recursiva
resultado = search(t.root, 5)
print(resultado.key if resultado else "Não encontrado")

# busca iterativa
resultado = iterative_search(t.root, 15)
print(resultado.key if resultado else "Não encontrado")

#inserção de nodes 
print(t.root.left.key) #5
print(t.root.right.key) #15