def countingSort(arr):
    # Passo 1: Encontra o maior valor no array
    max_val = max(arr)

    # Passo 2: Cria um array de contagem com zeros
    count = [0] * (max_val + 1)

    # Passo 3: Conta quantas vezes cada valor aparece no array
    for num in arr:
        count[num] += 1

    # Passo 4: Reconstrói o array ordenado com base na contagem
    index = 0
    for i in range(len(count)):
        while count[i] > 0:   # Enquanto houver ocorrências do número i
            arr[index] = i    # Coloca o número no array original
            index += 1
            count[i] -= 1     # Decrementa a contagem

# Exemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
countingSort(arr)
print("Array ordenado é:", arr)


# Vantagens do Counting Sort:

# Muito rápido para valores pequenos e inteiros.
# Estável: Mantém a ordem dos elementos iguais.
# Muito eficiente em arrays grandes com pouca variação de valores.


# Desvantagens do Counting Sort:

# Não funciona com números negativos diretamente: Precisa de adaptação.
# Só funciona para números inteiros (discretos): Não serve para strings ou floats diretamente.
# Pouco flexível: Não é uma escolha geral como Quick Sort ou Merge Sort.
