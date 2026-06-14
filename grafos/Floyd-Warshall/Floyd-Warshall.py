def floyd_warshall(matriz_adjacencia):
    V = len(matriz_adjacencia)
    
    # Inicializa a matriz de distâncias copiando a matriz de adjacência original
    # D^(0) no modelo do livro do Cormen
    distancias = [list(linha) for linha in matriz_adjacencia]
    
    # Loop triplo de Programação Dinâmica
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Se passar pelo vértice 'k' encurta o caminho de 'i' para 'j'
                if distancias[i][k] != float('inf') and distancias[k][j] != float('inf'):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
                    
    return distancias

# Exemplo Prático de Uso
if __name__ == "__main__":
    INF = float('inf')
    
    # Matriz de Adjacência de exemplo
    grafo_matriz = [
        [0,   3,   8,   INF, -4],
        [INF, 0,   INF, 1,   7],
        [INF, 4,   0,   INF, INF],
        [2,   INF, -5,  0,   INF],
        [INF, INF, INF, 6,   0]
    ]
    
    resultado = floyd_warshall(grafo_matriz)
    
    print("--- Algoritmo de Floyd-Warshall (Matriz de Distâncias Finais) ---")
    for i, linha in enumerate(resultado):
        print(f"Origem {i}: " + " ".join(f"{val:4}" if val != INF else " INF" for val in linha))