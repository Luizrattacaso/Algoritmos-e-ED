# Algoritmo de Bellman-Ford

Referência:
- Inglês: [Introduction to Algorithms - pg 651](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf#%5B%7B%22num%22%3A1318%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)
- Português: [Algoritmos Teoria e Prática - pg 531](https://computerscience360.wordpress.com/wp-content/uploads/2018/02/algoritmos-teoria-e-prc3a1tica-3ed-thomas-cormen.pdf#%5B%7B%22num%22%3A1863%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C56.66969%2C450.7266%2Cnull%5D)

## 1. O Problema do Caminho Mínimo com Pesos Negativos
Diferente do algoritmo de Dijkstra, o algoritmo de **Bellman-Ford** resolve o problema de caminhos mínimos de origem única em grafos onde as arestas podem possuir **pesos negativos**. O algoritmo também é capaz de detectar a existência de **ciclos de peso negativo** alcançáveis a partir da origem.

### Ideia Central do Algoritmo
O algoritmo utiliza a abordagem de Programação Dinâmica de forma iterativa. Ele relaxa sistematicamente todas as arestas do grafo $|V| - 1$ vezes. Essa quantidade de repetições garante que, na ausência de ciclos negativos, o caminho mínimo para qualquer vértice seja encontrado, já que o caminho mais longo possível sem ciclos possui no máximo $|V| - 1$ arestas.

### O Mecanismo de Detecção de Ciclos Negativos
Se após relaxar todas as arestas $|V| - 1$ vezes, ainda for possível realizar mais um relaxamento que diminua a distância estimada de algum vértice ($d[u] + w(u, v) < d[v]$), significa que o grafo contém um ciclo cuja soma dos pesos é menor que zero. Nesse caso, caminhos mínimos não são bem definidos, pois seria possível caminhar infinitamente pelo ciclo diminuindo o custo para $-\infty$.

## 2. Estrutura do Código
A implementação recebe uma lista explícita de arestas (no formato de tuplas `(u, v, peso)`), o que otimiza o laço principal de relaxamento ao evitar a navegação por listas de adjacências aninhadas.

### Complexidade
- **Tempo:** $O(V \cdot E)$. O algoritmo possui um laço externo que roda $|V| - 1$ vezes e um laço interno que percorre todas as $|E|$ arestas a cada iteração, seguido por uma verificação final de tamanho $|E|$.
- **Espaço:** $O(V)$ para rastrear os dicionários de `distancias` e `predecessores` de cada vértice.

## 3. Vantagem Crucial
> **DIFERENCIAL:** A principal vantagem de Bellman-Ford sobre o Dijkstra é sua versatilidade matemática para lidar com cenários financeiros ou de redes onde "ganhos" ou compensações são modelados como pesos negativos. Além disso, ele serve como base estrutural para algoritmos mais complexos de caminhos mínimos de todos os pares (como o Algoritmo de Johnson).

## 4. Como Executar
O script `bellman_ford.py` já vem com o exemplo clássico do livro do Cormen embutido (composto por 5 vértices e arestas negativas). Para rodar:

```bash
python bellman_ford.py