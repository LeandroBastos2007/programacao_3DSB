# Solicita ao usuário que digite um número inteiro
numero = int(input("__________________________: "))

# Verifica se o número é par
if numero % 2 == 0:
    # Se for par, imprime a mensagem
    print(f"{numero} é par.")
else:
    # Se for ímpar, imprime a mensagem
    print(f"{numero} é ______________.")

# Solicita um número ao usuário
numero = float(input("__________________________"))

# Verifica se o número é positivo
if numero > 0:
    # Se for positivo, imprime a mensagem
    print("O número é _________________.")
# Verifica se o número é negativo
elif numero < 0:
    # Se for negativo, imprime a mensagem
    print("_______________________________________")
# Se não for positivo nem negativo, é zero
else:
    # Imprime a mensagem para zero
    print("__________________________________")

