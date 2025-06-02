def selection_sort(lista):                         # Calcula o tamanho da lista
    n = len(lista)
    for j in range(n - 1):                         # Percorre da posição 0 até a penúltima
        minimo_indice = j                          # Assume que o menor elemento está na posição atual
        for i in range(j, n):                      # Procura o menor valor no restante da lista (do índice j até o fim)
            if lista[i] < lista[minimo_indice]:    # Se encontrar um valor menor
                minimo_indice = i                  # Atualiza o índice do menor valor

        if lista[j] > lista[minimo_indice]:        # Se o menor valor encontrado for diferente do atual (posição j),
            
            # Faz a troca                              # Fazemos a troca para colocar o menor valor na posição correta
            aux = lista[j]                             # Guardamos o valor atual em uma variável auxiliar
            lista[j] = lista[minimo_indice]            # Colocamos o menor valor na posição j
            lista[minimo_indice] = aux                 # Colocamos o valor antigo de j na posição do menor valor


lista = [7, 5, 1, 8, 3]
selection_sort(lista)
print(lista)


# Vantagens do Selection Sort:

# - Simples de Implementar
# - Funciona bem em listas pequenas, como de 5 a 10 elementos
# - Ideal para iniciantes em programação e algoritmos.


# Desvantagens do Selection Sort:

# - Lento para listas grandes, como de 1000 elementos
# - Não é estável
# - Ignora se a lista já está quase ordenada,
#   ele sempre faz a comparação do mesmo jeito,
#   ao contrário de outros algoritmos como o Insertion Sort ou Bubble Sort com otimização.