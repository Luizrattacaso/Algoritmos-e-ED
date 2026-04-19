from Classes import Tree, Node
from operacoes_basicas.search import search, iterative_search
from operacoes_basicas.Simple_insert import insert_node
from operacoes_basicas.Successor import Successor

t = Tree()

t.root = Node(10)

insert_node(t, Node(5))
insert_node(t, Node(15))
insert_node(t, Node(6))
insert_node(t, Node(7))
insert_node(t, Node(16))

# busca recursiva
resultado = search(t.root, 5)
print(resultado.key if resultado else "Não encontrado")

# busca iterativa
resultado = iterative_search(t.root, 15)
print(resultado.key if resultado else "Não encontrado")

#inserção de nodes 
print(t.root.left.key) #5
print(t.root.right.key) #15
print(Successor(t.root.right).key)