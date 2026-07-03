# Dados representados por tuplas (tipo, nome)
cadastro = [
    ("Cão", "Thor"),
    ("Gato", "Luna")
]

# Função pura para obter o som baseado no tipo
def obter_som(animal):
    sons = {"Cão": "Au Au!", "Gato": "Miau!"}
    return sons.get(animal[0], "Som desconhecido")

# Função pura para formatar o registro
def formatar_registro(animal):
    return f"Animal: {animal[1]} ({animal[0]}) - Som: {obter_som(animal)}"

# Aplicação de Programação Funcional (map)
relatorio = list(map(formatar_registro, cadastro))

# Exibição dos resultados
print("\n".join(relatorio))
