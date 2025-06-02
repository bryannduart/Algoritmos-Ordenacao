def bucketSort(arr):
    n = len(arr)  # Tamanho do array

    if n == 0:
        return  # Se o array estiver vazio, não faz nada

    # Passo 1: Cria n "baldes" vazios (listas)
    buckets = [[] for _ in range(n)]

    # Passo 2: Distribui os elementos nos baldes com base no valor
    for num in arr:
        index = int(num * n)  # Calcula em qual balde o número entra
        buckets[index].append(num)

    # Passo 3: Ordena individualmente cada balde (usando sort interno do Python)
    for bucket in buckets:
        bucket.sort()

    # Passo 4: Junta todos os baldes em um único array ordenado
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num  # Copia os elementos ordenados de volta
            index += 1

# Exemplo de uso (valores entre 0 e 1)
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucketSort(arr)
print("Array ordenado é:", arr)


# Vantagens do Bucket Sort:

# Muito rápido com dados uniformemente distribuídos (ex: números decimais entre 0 e 1).
# Estável: Se a ordenação interna for estável.
# Paralelizável: Cada balde pode ser ordenado separadamente.


# Desvantagens do Bucket Sort:

# Funciona melhor com números entre 0 e 1: Fora disso, precisa adaptar.
# Requer memória extra para os baldes: Pode ser um problema para listas grandes.
# Precisa escolher bem o número de baldes: Muito ou pouco afeta o desempenho.