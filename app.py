# Entrada dos dados 
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em Watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
tarifa = 0.75
custo_estimado = consumo_mensal * tarifa

# Saidas  dos resultados formatados
print("\n" + "="*30)
print("Aparelho: nome_aparelho")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f}")
