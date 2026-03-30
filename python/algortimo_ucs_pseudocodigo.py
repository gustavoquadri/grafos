import heapq

def ucs(grafo, inicio, objetivo):
    # fila de prioridade: (custo_acumulado, no_atual, caminho)
    fila = []
    heapq.heappush(fila, (0, inicio, [inicio]))
    
    # dicionário para guardar o menor custo já encontrado
    visitados = {}

    while fila:
        custo, no, caminho = heapq.heappop(fila)
        print(grafo[no])

        # se já visitamos com custo menor, ignoramos
        if no in visitados and visitados[no] <= custo:
            continue
        
        visitados[no] = custo

        # se chegou no objetivo, retorna
        if no == objetivo:
            return caminho, custo

        # expande os vizinhos
        for vizinho, custo_aresta in grafo[no]:
            novo_custo = custo + custo_aresta
            heapq.heappush(fila, (novo_custo, vizinho, caminho + [vizinho]))

    return None, float("inf")


grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

caminho, custo = ucs(grafo, 'A', 'D')

print("Caminho:", caminho)
print("Custo:", custo)
