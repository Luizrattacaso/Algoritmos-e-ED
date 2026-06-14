import heapq

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    predecessores = {v: None for v in grafo}
    distancias[origem] = 0

    fila_prioridade = [(0, origem)]
    vertices_visitados = set()

    while fila_prioridade:
        dist_u, u = heapq.heappop(fila_prioridade)
        
        if u in vertices_visitados:
            continue
        vertices_visitados.add(u)
        
        for vizinho, peso in grafo[u].items():
            if distancias[u] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[u] + peso
                predecessores[vizinho] = u
                heapq.heappush(fila_prioridade, (distancias[vizinho], vizinho))
                
    return distancias, predecessores

# Exemplo Prático de Uso
if __name__ == "__main__":
    # Representação por Lista de Adjacência
    grafo_exemplo = {
        's': {'t': 10, 'y': 5},
        't': {'x': 1, 'y': 2},
        'x': {'z': 4},
        'y': {'t': 3, 'x': 9, 'z': 2},
        'z': {'x': 6, 's': 7}
    }
    
    origem_no = 's'
    dist, pred = dijkstra(grafo_exemplo, origem_no)
    
    print(f"--- Algoritmo de Dijkstra (Origem: {origem_no}) ---")
    for no in dist:
        print(f"Vértice: {no} | Distância Mínima: {dist[no]} | Predecessor: {pred[no]}")