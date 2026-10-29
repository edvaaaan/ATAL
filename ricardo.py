# QUESTAO A (DIVISAO DA SORTE)
def eh_quase_da_sorte(n):
    # Todos os números da sorte até 1000
    numeros_da_sorte = [
        4, 7, 
        44, 47, 74, 77, 
        444, 447, 474, 477, 744, 747, 774, 777
    ]
    
    # Verifica se n é divisível por algum número da sorte
    for sorte in numeros_da_sorte:
        if n % sorte == 0:
            return "YES"
            
    return "NO"

# Leitura da entrada
n = int(input().strip())
print(eh_quase_da_sorte(n))

# QUESTAO B (SOMA SUBARRAYS)
def soma_subarrays_impares(n, arr):
    soma_total = 0
    
    for i in range(n):
        # Número de subarrays que contêm o elemento arr[i]
        total_subarrays = (i + 1) * (n - i)
        
        # Quantidade desses subarrays que possuem tamanho ímpar
        subarrays_impares = (total_subarrays + 1) // 2
        
        # Adiciona a contribuição do elemento atual à soma total
        soma_total += arr[i] * subarrays_impares
        
    return soma_total

# Leitura da entrada
n = int(input().strip())
arr = list(map(int, input().split()))

print(soma_subarrays_impares(n, arr))

# QUESTAO C
def encontrar_k_esima_string_feliz(n, k):
    resultado = []
    contador = 0

    def backtracking(string_atual):
        nonlocal contador
        # Se atingimos o tamanho desejado n, incrementamos o contador
        if len(string_atual) == n:
            contador += 1
            if contador == k:
                resultado.append(string_atual)
            return

        # Testa as opções de letras na ordem lexicográfica ('a', 'b', 'c')
        for opcao in ['a', 'b', 'c']:
            # Só adicionamos a opção se ela não for igual ao último caractere adicionado
            if not string_atual or string_atual[-1] != opcao:
                backtracking(string_atual + opcao)
                # Se já encontramos a k-ésima string, podemos interromper a busca antecipadamente
                if resultado:
                    return

    backtracking("")
    
    # Se encontramos a k-ésima string, retornamos ela; caso contrário, "vazio"
    return resultado[0] if resultado else "vazio"

# Leitura da entrada
n, k = map(int, input().split())
print(encontrar_k_esima_string_feliz(n, k))

# QUESTAO D
import math

# Leitura do tamanho do vetor
n = int(input().strip())

# Leitura dos elementos (necessária para consumir a linha da entrada)
nums = list(map(int, input().split()))

# O número de permutações de n elementos distintos é n!
quantidade_permutacoes = math.factorial(n)

print(quantidade_permutacoes)
