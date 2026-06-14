import heapq

def dijkstra_johnson(grafo, origem, V):
    """Função auxiliar de Dijkstra modificada para o algoritmo de Johnson."""
    distancias = [float('inf')] * V
    distancias[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        d, u = heapq.heappop(fila)
        if d > distancias[u]:
            continue
        for v, peso in grafo[u]:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                heapq.heappush(fila, (distancias[v], v))
    return distancias

def bellman_ford_johnson(arestas, V):
    """Função auxiliar de Bellman-Ford estendida com super-vértice s virtual."""
    distancias = [0] * (V + 1) # s está no índice V
    
    # Criar cópia e adicionar arestas direcionadas de custo 0 do vértice virtual V para todos os outros
    arestas_virtuais = list(arestas)
    for i in range(V):
        arestas_virtuais.append((V, i, 0))
        
    # Relaxar as arestas V vezes
    for _ in range(V):
        for u, v, peso in arestas_virtuais:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                
    # Detectar ciclo negativo
    for u, v, peso in arestas_virtuais:
        if distancias[u] + peso < distancias[v]:
            return None
            
    return distancias[:V] # Retorna h[u] apenas para os vértices reais

def johnson(arestas, V):
    # Passo 1: Executa Bellman-Ford com vértice virtual para achar função potencial h
    h = bellman_ford_johnson(arestas, V)
    if h is None:
        print("Erro: O grafo contém um ciclo de peso negativo!")
        return None
        
    # Passo 2: Reponderar o grafo original para garantir pesos não-negativos:
    # w'(u, v) = w(u, v) + h[u] - h[v]
    grafo_reponderado = {i: [] for i in range(V)}
    pesos_originais = {}
    
    for u, v, peso in arestas:
        peso_novo = peso + h[u] - h[v]
        grafo_reponderado[u].append((v, peso_novo))
        pesos_originais[(u, v)] = peso
        
    # Passo 3: Rodar Dijkstra uma vez para cada vértice como origem única
    matriz_distancias = []
    for u in range(V):
        dist_reponderadas = dijkstra_johnson(grafo_reponderado, u, V)
        
        # Devolver ao peso original: d(u, v) = d'(u, v) + h[v] - h[u]
        dist_reais = []
        for v in range(V):
            if dist_reponderadas[v] == float('inf'):
                dist_reais.append(float('inf'))
            else:
                dist_reais.append(dist_reponderadas[v] + h[v] - h[u])
        matriz_distancias.append(dist_reais)
        
    return matriz_distancias

# Exemplo Prático de Uso
if __name__ == "__main__":
    INF = float('inf')
    num_vertices = 5
    
    # Grafo em formato de Lista de Arestas (u, v, peso) - ID Numérico (0-4)
    arestas_exemplo = [
        (0, 1, 3), (0, 2, 8), (0, 4, -4),
        (1, 3, 1), (1, 4, 7),
        (2, 1, 4),
        (3, 0, 2), (3, 2, -5),
        (4, 3, 6)
    ]
    
    matriz_final = johnson(arestas_exemplo, num_vertices)
    
    if matriz_final:
        print("--- Algoritmo de Johnson (Matriz de Todos os Pares) ---")
        for i, linha in enumerate(matriz_final):
            print(f"Origem {i}: " + " ".join(f"{val:4}" if val != INF else " INF" for val in linha))