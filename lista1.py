# Passo 1: Recebe o número inteiro positivo n
n = int(input("Digite a quantidade de números (n): "))

# Passo 2: Lê n números inteiros e os adiciona em uma lista
lista = []
for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    lista.append(num)

# Passo 3: Recebe um número x e verifica se ele está na lista
x = int(input("Digite o número x para verificar: "))

if x in lista:
    print(f"O número {x} pertence à lista.")
else:
    print(f"O número {x} NÃO pertence à lista.")
