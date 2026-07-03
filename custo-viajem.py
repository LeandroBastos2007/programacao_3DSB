def calcular_custo_total_viagem(veiculos, distancia=200):
    """
    Calcula o custo total de uma viagem para uma lista de veículos.
    Assume que cada objeto veículo possui um atributo 'custo_por_km'.
    """
    custo_total = 0
    
    for veiculo in veiculos:
        # Calcula o custo individual e soma ao total
        custo_total += veiculo.custo_por_km * distancia
        
    return custo_total

# Exemplo de como estruturar os objetos e usar a função:
class Veiculo:
    def __init__(self, nome, custo_por_km):
        self.nome = nome
        self.custo_por_km = custo_por_km

# Criando a lista de objetos
frota = [
    Veiculo("Carro", 0.50),
    Veiculo("Caminhão", 1.20),
    Veiculo("Moto", 0.25)
]

# Chamando a função
resultado = calcular_custo_total_viagem(frota)
print(f"O custo total para todos os veículos percorrerem 200 km é: R$ {resultado:.2f}")
