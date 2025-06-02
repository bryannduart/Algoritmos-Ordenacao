# Função principal do Quick Sort
def quicksort(lista, inicio=0, fim=None):
    # Define o índice final caso não seja passado
    if fim is None:
        fim = len(lista) - 1

    # Só continua se houver pelo menos dois elementos na sublista
    if inicio < fim:
        # Chama a função partition para reorganizar os elementos
        # e obter o índice do pivô na posição correta
        p = partition(lista, inicio, fim)

        # Ordena recursivamente a sublista à esquerda do pivô
        quicksort(lista, inicio, p - 1)

        # Ordena recursivamente a sublista à direita do pivô
        quicksort(lista, p + 1, fim)

# Função responsável por particionar a lista e colocar o pivô na posição certa
def partition(lista, inicio, fim):
    # Define o pivô como o último elemento do intervalo
    pivot = lista[fim]

    # Índice para rastrear a "fronteira" dos elementos menores ou iguais ao pivô
    i = inicio

    # Percorre todos os elementos da sublista (exceto o pivô)
    for j in range(inicio, fim):
        # Compara cada elemento com o pivô
        if lista[j] <= pivot:
            # Se o elemento for menor ou igual ao pivô, troca de posição
            lista[j], lista[i] = lista[i], lista[j]
            # Move a fronteira para frente
            i += 1

    # Coloca o pivô na posição correta (entre os menores e os maiores)
    lista[i], lista[fim] = lista[fim], lista[i]

    # Retorna o índice final do pivô
    return i


# Vantagens do Quick Sort:

# Muito rápido na prática: Geralmente é mais rápido que Merge Sort e outros algoritmos, especialmente em listas grandes.
# Desempenho excelente em médias e grandes listas: Ótimo para uso geral, especialmente quando os dados cabem na memória.
# Uso de memória eficiente: É um algoritmo in-place, ou seja, não precisa de memória adicional significativa além da pilha de chamadas recursivas.


# Desvantagens do Quick Sort:

# Não é estável: Elementos iguais podem trocar de ordem, o que é ruim para certos tipos de ordenação (como ordenação por múltiplas chaves).
# Pode ser lento em listas pequenas: Para listas com poucos elementos, pois o Quick Sort tem mais "trabalho extra" (funções, trocas e chamadas recursivas).
# Não ideal para dados quase ordenados: Se a lista já estiver quase ordenada, o Quick Sort pode acabar fazendo muito mais trabalho do que o necessário.