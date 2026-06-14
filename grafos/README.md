# Grafos

Este módulo contém implementações didáticas e documentações detalhadas sobre algoritmos de caminhos mínimos em grafos, baseando-se estritamente nos capítulos 22 a 26 do livro **"Introduction to Algorithms" (Cormen et al.)**.

## 1. Definição Formal de Grafos
Um **Grafo** $G$ é um par ordenado $G = (V, E)$, onde:
- $V$ é um conjunto não-vazio de **vértices** (ou nós).
- $E$ é um conjunto de **arestas** (ou arcos), composto por pares de elementos de $V$, ou seja, $E \subseteq V \times V$.

### Diferença entre Grafo e Árvore
Uma **árvore** é simplesmente um tipo especial de grafo. Formalmente, uma árvore é um grafo não-direcionado, **conexo** e **acíclico**.

```
   [Grafo Acíclico / Árvore]           [Grafo Cíclico / Não-Árvore]
           (A)                                     (A)
          /   \                                   /   \
        (B)   (C)                               (B)---(C)
        /                                       /
      (D)                                     (D)
```

## 2. Classificações de Grafos

1. **Direcionado (Dígrafo) vs. Não-Direcionado:** No direcionado, as arestas possuem um sentido $(u \to v \neq v \to u)$. No não-direcionado, a relação é simétrica.
2. **Ponderado vs. Não-Ponderado:** No ponderado, cada aresta possui um peso associado $w(u, v) \in \mathbb{R}$ (custo, distância, tempo).
3. **Cíclico vs. Acíclico:** Um grafo é cíclico se contém pelo menos um caminho que começa e termina no mesmo vértice. Caso contrário, é acíclico (ex: DAGs).

## 3. Representações Computacionais

### Matriz de Adjacência

Uma matriz $A$ de dimensões $|V| \times |V|$ onde $A[i][j]$ armazena o peso da aresta (ou 1 se existir e 0 caso contrário).

* **Espaço:** $O(V^2)$ ---> Melhor para grafos densos
* **Verificar se $(u,v) \in E$:** $O(1)$
* **Listar vizinhos de $u$:** $O(V)$
* *Ideal para:* Grafos densos ($|E| \approx |V|^2$).

### Lista de Adjacência

Um array ou dicionário de tamanho $|V|$ onde cada posição $u$ aponta para uma lista de seus vértices adjacentes.

* **Espaço:** $O(V + E)$ ---> Melhor para grafos esparços
* **Verificar se $(u,v) \in E$:** $O(\text{grau}(u))$
* **Listar vizinhos de $u$:** $O(\text{grau}(u))$
* *Ideal para:* Grafos esparsos ($|E| \ll |V|^2$).

---

## 4. Tabela Comparativa de Algoritmos (Caminhos Mínimos)

| Algoritmo | Complexidade Tempo | Complexidade Espaço | Quando Usar | Restrições / Condições |
| --- | --- | --- | --- | --- |
| **Dijkstra** (com Min-Heap) | $O((V + E) \log V)$ | $O(V + E)$ | Caminho mínimo de origem única em grafos com pesos positivos. | **Não aceita pesos negativos**. |
| **Bellman-Ford** | $O(V \cdot E)$ | $O(V + E)$ | Caminho mínimo de origem única; detecção de ciclos negativos. | Mais lento; aceita pesos negativos. |
| **Floyd-Warshall** | $O(V^3)$ | $O(V^2)$ | Caminhos mínimos entre todos os pares de vértices em grafos densos. | Simples de implementar; aceita pesos negativos (sem ciclos). |
| **Johnson** | $O(V^2 \log V + V \cdot E)$ | $O(V^2)$ | Caminhos mínimos entre todos os pares de vértices em grafos esparsos. | Melhor que Floyd-Warshall se o grafo for esparso. |

---

## 5. Casos de Uso Reais

* **Sistemas de GPS e Mapas:** Cálculo da rota mais rápida entre duas cidades (Dijkstra/A*).
* **Redes de Computadores:** Protocolos de roteamento OSPF utilizam Dijkstra para achar caminhos mais curtos para pacotes de dados.
* **Redes Sociais:** Sugestão de conexões por nível de distância/proximidade ("amigos em comum").
* **Logística e Cadeia de Suprimentos:** Otimização de frotas e entrega de mercadorias.

```

```