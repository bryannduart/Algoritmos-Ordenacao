# Função auxiliar que faz Counting Sort baseado no dígito atual (unidade, dezena, etc)
def countingSortPorDigito(arr, exp):
    n = len(arr)  # Tamanho do array
    output = [0] * n  # Cria um array de saída com zeros
    count = [0] * 10  # Cria array de contagem (para os dígitos de 0 a 9)

    # Conta quantas vezes cada dígito aparece na posição atual (exp)
    for i in range(n):
        indice = (arr[i] // exp) % 10  # Pega o dígito da posição atual
        count[indice] += 1  # Incrementa a contagem desse dígito

    # Converte count[] para posições acumuladas (posição correta dos números)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Monta o array de saída em ordem com base no dígito atual
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10  # Pega o dígito novamente
        output[count[indice] - 1] = arr[i]  # Coloca o número na posição correta
        count[indice] -= 1  # Atualiza a contagem
        i -= 1  # Vai para o próximo elemento (de trás para frente)

    # Copia o array ordenado de volta para o array original
    for i in range(n):
        arr[i] = output[i]

# Função principal do Radix Sort
def radixSort(arr):
    max_val = max(arr)  # Encontra o maior número para saber o número de dígitos

    exp = 1  # Começa pela unidade (10^0)
    while max_val // exp > 0:  # Continua enquanto houver dígitos
        countingSortPorDigito(arr, exp)  # Ordena pelo dígito atual
        exp *= 10  # Passa para o próximo dígito (dezenas, centenas, ...)

# Exemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print("Array ordenado é:", arr)


# Vantagens do Radix Sort:

# Estável: Mantém a ordem dos elementos com mesmo valor.
# Não usa comparações diretas entre os elementos.
# Bom para grandes volumes de dados com tamanho de valor limitado – Ex: CPF, matrícula, ID, etc.


# Desvantagens do Radix Sort:

# Só funciona com números inteiros: Para strings ou floats, precisa adaptação.
# Não funciona bem se os números tiverem muitos dígitos: Vira ineficiente.
# Código mais complexo que algoritmos simples (como Bubble ou Insertion Sort).