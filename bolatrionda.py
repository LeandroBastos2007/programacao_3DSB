# Variáveis de entrada (exemplos de valores para teste)
bateria_atual = 10  # Inteiro de 0 a 100
bola_em_jogo = True # Booleano (True ou False)

# Lógica do Sistema de Alarme
if bateria_atual < 15 and bola_em_jogo == True:
    print('ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.')

elif bateria_atual < 15 and bola_em_jogo == False:
    print('Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.')

else:
    print('Sistema Trionda operando normalmente. Bateria ok.')
