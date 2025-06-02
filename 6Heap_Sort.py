# Função para "ajustar" o heap (heapify) de uma árvore binária
def heapify(arr, n, i):
    largest = i            # Inicializa o maior como a raiz
    left = 2 * i + 1       # Índice do filho da esquerda
    right = 2 * i + 2      # Índice do filho da direita

    # Se o filho da esquerda for maior que a raiz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Se o filho da direita for maior que o maior até agora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca os elementos
        heapify(arr, n, largest)  # Aplica o heapify recursivamente

# Função principal que implementa o Heap Sort
def heapSort(arr):
    n = len(arr)  # Obtém o tamanho da lista

    # Constrói um Max-Heap (do meio até a raiz)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Um por um, remove os elementos do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o primeiro (maior) com o último
        heapify(arr, i, 0)  # Reorganiza o heap reduzido

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Array ordenado é:", arr)


# Vantagens do Heap Sort:

# Não usa muita memória extra: Ordena os dados no próprio array (in-place).
# Independente da ordem inicial dos dados: Funciona bem mesmo se o array estiver quase ordenado ou totalmente bagunçado.
# Funciona bem com grandes quantidades de dados.


# Desvantagens do Heap Sort:

# Implementação um pouco mais complexa: Comparado a algoritmos mais simples como Insertion Sort ou Bubble Sort.
# Não é estável: Não mantém a ordem dos elementos iguais.
# Mais lento que outros algoritmos na prática: Como Quick Sort ou Merge Sort, em arrays comuns.


