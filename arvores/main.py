from Classes import Tree, Node
from operacoes_basicas.search import search, iterative_search

t = Tree()

t.root = Node(10)
t.root.left = Node(5)
t.root.right = Node(15)

# busca recursiva
resultado = search(t.root, 5)
print(resultado.key if resultado else "Não encontrado")

# busca iterativa
resultado = iterative_search(t.root, 15)
print(resultado.key if resultado else "Não encontrado")