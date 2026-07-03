class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método especial para representação textual do objeto
    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.paginas}"

# Solicitação de dados ao usuário
print("--- Cadastro de Livro ---")
titulo_input = input("Digite o título do livro: ")
autor_input = input("Digite o autor do livro: ")
paginas_input = input("Digite a quantidade de páginas: ")

# Instanciação do objeto
novo_livro = Livro(titulo_input, autor_input, paginas_input)

# Exibição da descrição formatada utilizando o método __str__()
print("\n--- Informações do Livro Cadastrado ---")
print(novo_livro)
