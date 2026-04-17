import random

def jogar():
    palavras = "python java javascript ruby php csharp".split()
    palavra_secreta = random.choice(palavras).lower()
    letras_acertadas = ["_" for _ in palavra_secreta]
    erros = 0
    tentativas = ""

    print("Bem-vindo ao Jogo da Forca!")

    while erros < 6 and "_" in letras_acertadas:
        print(desenhar_forca(erros))
        print(f"Palavra: {' '.join(letras_acertadas)}")
        print(f"Letras tentadas: {tentativas.upper()}")
        
        chute = input("Qual letra? ").strip().lower()

        if chute in tentativas:
            print("Você já tentou essa letra!")
            continue
        
        tentativas += chute

        if palavra_secreta.find(chute) != -1:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_acertadas[i] = chute
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

    if "_" not in letras_acertadas:
        print(f"\nParabéns! Você ganhou. A palavra era: {palavra_secreta.upper()}")
    else:
        print(desenhar_forca(erros))
        print(f"\nGame Over! A palavra era: {palavra_secreta.upper()}")

def desenhar_forca(erros):
    estagios = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |",  # Inicial
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |",  # Cabeça
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |",  # Tronco
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |",  # Braço Esquerdo
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |",  # Braço Direito
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |",  # Perna Esquerda
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |"   # Perna Direita
    ]
    return estagios[erros]

jogar()
