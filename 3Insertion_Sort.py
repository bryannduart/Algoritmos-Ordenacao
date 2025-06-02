def insertion_sort(lista):
    n = len(lista)                               # Obtém o tamanho da lista
    for i in range(1, n):                        # Começa do segundo elemento (índice 1) até o final da lista
        chave = lista[i]                         # Guarda o valor atual que queremos posicionar corretamente
        j = i - 1                                # Começa comparando com o elemento anterior ao atual
        
        # Enquanto j for válido (>= 0) e o valor em lista[j] for maior que a chave,
        # desloca os elementos para a direita
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]                # Move o elemento maior uma posição à frente
            j = j - 1                            # Anda para a esquerda na lista
        
        # Quando encontrar a posição correta (ou chegar no início da lista),
        # insere a chave nessa posição
        lista[j+1] = chave

lista = [4, 7, 2, 5, 4, 0]
insertion_sort(lista)
print(lista)


# Vantagens do Insertion Sort:

# -Simples de implementar: O algoritmo é direto, fácil de entender e de programar.
# -Eficiente para listas pequenas: Para poucos elementos, pode ser mais rápido que algoritmos mais complexos como Quick Sort ou Merge Sort.
# -Pouco uso de memória: É um algoritmo in-place, ou seja, não precisa de espaço extra além da lista original.


# Desvantagens do Insertion Sort:

# -Ineficiente para listas grandes: Muito lento quanto a lista tem muitos elementos.
# -Pouco escalável: Outras abordagens (como Merge Sort ou Quick Sort) são muito mais rápidas para listas grandes.
# -Não aproveita paralelismo: A natureza sequencial do algoritmo não favorece execução paralela (multi-threading), que é quando divide o trabalho em várias tarefas.