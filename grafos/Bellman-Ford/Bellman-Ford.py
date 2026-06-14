def bellman_ford(arestas, origem, num_vertices, vertices):
    # Passo 1: Inicialização (INITIALIZE-SINGLE-SOURCE)
    distancias = {v: float('inf') for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[origem] = 0
    
    # Passo 2: Relaxar todas as arestas |V| - 1 vezes repetidamente
    for _ in range(num_vertices - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u
                
    # Passo 3: Verificação de ciclos de peso negativo
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            print("Aviso: O grafo contém um ciclo de peso negativo alcançável a partir da origem!")
            return None, None # Retorna None se houver ciclo negativo
            
    return distancias, predecessores

# Exemplo Prático de Uso
if __name__ == "__main__":
    # Lista de Vértices
    lista_vertices = ['s', 't', 'x', 'y', 'z']
    
    # Representação por Lista de Arestas (u, v, peso)
    arestas_exemplo = [
        ('s', 't', 6), ('s', 'y', 7),
        ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
        ('x', 't', -2),
        ('y', 'x', -3), ('y', 'z', 9),
        ('z', 's', 2), ('z', 'x', 7)
    ]
    
    origem_no = 's'
    dist, pred = bellman_ford(arestas_exemplo, origem_no, len(lista_vertices), lista_vertices)
    
    if dist:
        print(f"--- Algoritmo de Bellman-Ford (Origem: {origem_no}) ---")
        for no in dist:
            print(f"Vértice: {no} | Distância Mínima: {dist[no]} | Predecessor: {pred[no]}")