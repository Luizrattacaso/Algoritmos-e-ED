# Algoritmo de Dijkstra

Referência:
- Inglês: [Introduction to Algorithms - pg 658](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf#%5B%7B%22num%22%3A1332%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)
- Português: [Algoritmos Teoria e Prática - pg 537](https://computerscience360.wordpress.com/wp-content/uploads/2018/02/algoritmos-teoria-e-prc3a1tica-3ed-thomas-cormen.pdf#%5B%7B%22num%22%3A1882%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C56.66969%2C369.6914%2Cnull%5D)

## 1. O Problema do Caminho Mínimo de Origem Única
Dado um grafo direcionado e ponderado $G = (V, E)$ e um vértice de origem $s \in V$, o algoritmo de Dijkstra encontra o caminho de menor custo (menor soma de pesos das arestas) de $s$ para todos os outros vértices $v \in V$.

### Ideia Central do Algoritmo
O algoritmo é do tipo **ganancioso (greedy)**. Ele mantém um conjunto $S$ de vértices cujos pesos finais de caminhos mínimos desde a origem já foram determinados. Repetidamente, o algoritmo seleciona o vértice $u \in V - S$ que possui a menor estimativa de caminho mínimo, adiciona $u$ ao conjunto $S$ e **relaxa** todas as arestas que saem de $u$.

### O que é o Relaxamento (RELAX)?
O relaxamento é a operação que testa se é possível melhorar o caminho mais curto para um vértice $v$ passando por um vértice intermediário $u$.
Formulando matematicamente:
$$if\ d[u] + w(u, v) < d[v]:\ d[v] = d[u] + w(u, v)$$

## 2. Estrutura do Código
A implementação utiliza uma **Fila de Prioridades (Min-Heap)** através do módulo nativo `heapq` do Python para garantir a seleção eficiente do próximo vértice com a menor distância estimada.

### Complexidade
- **Tempo:** $O((V + E) \log V)$ usando Min-Heap. Cada uma das $|V|$ operações `extract-min` leva $O(\log V)$ e o relaxamento das $|E|$ arestas pode invocar uma atualização no heap que custa $O(\log V)$.
- **Espaço:** $O(V + E)$ para armazenar a lista de adjacências do grafo e as estruturas auxiliares (`distancias`, `predecessores` e o Heap).

## 3. Restrição Crucial
> **IMPORTANTE:** O algoritmo de Dijkstra exige que os pesos de todas as arestas sejam **não-negativos** ($w(u, v) \geq 0$). Se o seu grafo contiver arestas com pesos negativos, é melhor usar o algoritmo de **Bellman-Ford**.

## 4. Como Executar
O script `dijkstra.py` já vem com o exemplo clássico do livro do Cormen embutido. Para rodar:

```bash
python dijkstra.py