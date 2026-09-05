print("Calculadora de Consumo Inteligente\n")

# Entrada dos dados
aparelho_nome = input("Digite o nome do aparelho: ")
aparelho_potencia = float(input("Digite a potência do aparelho (em W): "))
aparelho_uso = float(input("Digite o tempo médio de uso por dia (em h): "))

# Processamento
consumo_mes = (aparelho_potencia * aparelho_uso * 30) / 1000
custo_mes = consumo_mes * 0.75

# Resultado
print(f"\nAparelho: {aparelho_nome} \nConsumo mensal: {consumo_mes} kWh/mês"
f"\nCusto por mes: R${custo_mes:.2f}")