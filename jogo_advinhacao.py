import random

# Configurações iniciais
numero_secreto = random.randint(1, 10)
tentativas_restantes = 5
tentativa_atual = 1

print("--- Jogo de Adivinhação ---")
print("Tente adivinhar o número entre 1 e 10.")

while tentativa_atual <= tentativas_restantes:
    print(f"\nTentativa {tentativa_atual} de {tentativas_restantes}")
    chute = int(input("Digite seu palpite: "))

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break
    else:
        # Lógica do bônus: diferença de apenas 1 unidade
        if abs(chute - numero_secreto) == 1:
            tentativas_restantes += 1
            print("Você chegou muito perto! Ganhou +1 tentativa de bônus.")
        
        if tentativa_atual == tentativas_restantes:
            print(f"Suas tentativas acabaram. O número era {numero_secreto}.")
        else:
            print("Errado! Tente novamente.")
    
    tentativa_atual += 1
