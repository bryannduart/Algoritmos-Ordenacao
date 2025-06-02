# Função principal do Merge Sort
def mergesort(lista, inicio=0, fim=None):
    # Define o valor final da lista se não for fornecido
    if fim is None:
        fim = len(lista)
    
    # Verifica se o trecho da lista tem mais de um elemento
    if (fim - inicio > 1):
        # Calcula o meio do trecho da lista
        meio = (fim + inicio) // 2
        
        # Chamada recursiva para ordenar a primeira metade
        mergesort(lista, inicio, meio)
        
        # Chamada recursiva para ordenar a segunda metade
        mergesort(lista, meio, fim)
        
        # Junta as duas metades já ordenadas
        merge(lista, inicio, meio, fim)

# Função que junta (merge) duas sublistas ordenadas
def merge(lista, inicio, meio, fim):
    # Cria cópias das sublistas esquerda e direita
    left = lista[inicio:meio]
    right = lista[meio:fim]
    
    # Índices para percorrer as sublistas
    top_left, top_right = 0, 0
    
    # Percorre o trecho da lista original para inserir os elementos ordenados
    for k in range(inicio, fim):
        # Se todos os elementos da sublista esquerda já foram usados
        if top_left >= len(left):
            lista[k] = right[top_right]  # Insere elemento da direita
            top_right += 1
        # Se todos os elementos da sublista direita já foram usados
        elif top_right >= len(right):
            lista[k] = left[top_left]   # Insere elemento da esquerda
            top_left += 1
        # Se o próximo elemento da esquerda é menor que o da direita
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]   # Insere elemento da esquerda
            top_left += 1
        # Se o próximo elemento da direita é menor ou igual ao da esquerda
        else:
            lista[k] = right[top_right]  # Insere elemento da direita
            top_right += 1


# Vantagens do Merge Sort

# Bom para listas grandes ou arquivos externos (divisão e mesclagem são eficientes).
# Estável: mantém a ordem de elementos iguais.
# Funcionamento previsível, sem pior caso degradado como o Quick Sort.


# Desvantagens do Merge Sort

# Mais lento em listas pequenas que algoritmos como Insertion Sort, por causa da sobrecarga das chamadas recursivas.
# Complexidade na implementação: é mais difícil de entender e implementar que métodos simples como Bubble Sort.
# Uso extra de memória: precisa de espaço adicional proporcional ao tamanho da lista