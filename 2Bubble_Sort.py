def bubble_sort(lista):                             # Calcula o tamanho da lista
    n = len(lista)
    for j in range(n - 1):                          # Percorre da posição 0 até a penúltima
        for i in range(n - 1):                      # Percorre a lista comparando pares de elementos vizinhos
            if lista[i] > lista[i+1]:               # Compara o elemento atual com o próximo
                
                # Se estiver fora de ordem, faz a troca
                # Troca lista[i] com lista[i + 1]
                lista[i], lista[i+1] = lista[i+1], lista[i]


# Exemplo de ordenação de lista:
lista = [4, 9, 2, 1, 7, 8]
bubble_sort(lista)
print(lista)


# Vantagens do Bubble Sort:

# - Fácil de entender e implementar.
# - É otimizado, se em uma passada nenhuma troca for feita,
#   o algoritmo pode parar mais cedo, melhorando o desempenho.


# Desvantagens do Bubble Sort:

# - Muito lento para listas grandes, como de 10.000 elementos, pode haver até milhões de comparações.
# - Faz comparações desnecessárias:
#   Mesmo que os últimos elementos já estejam no lugar certo,
#   o algoritmo continua verificando todos os pares (a menos que otimizemos).
# - Desempenho pior que outros algoritmos:
#   Mesmo comparado com outros algoritmos simples,
#   o Bubble Sort costuma ser mais lento.
