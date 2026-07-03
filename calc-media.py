def calcular_media(numeros):
    if not numeros:
        return 0
    soma = sum(numeros)
    return soma / len(numeros)

# Função principal (main)
def main():
    numeros = [10, 20, 30, 40, 50]
    
    media = calcular_media(numeros)
    
    print(f"A média é: {media:.2f}")

if __name__ == "__main__":
    main()
