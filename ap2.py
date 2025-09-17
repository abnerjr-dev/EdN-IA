print("\n1- Conversor de Moeda")

real = 100  # float(input("Digite o valor em Reais (R$): "))
taxa_dolar = 5.20
taxa_euro = 6.15

dolares = real / taxa_dolar
euros = real / taxa_euro

print(f"Valor em Reais (R$): {real:.2f}")
print(f"Valor em Dólares (US$): {dolares:.2f}")
print(f"Valor em Euros (€): {euros:.2f}")

print("\n2- Calculadora de Desconto")

nome_produto = "Camiseta"  # input("Digite o nome do produto: ")
preco_original = 50  # float(input("Digite o preço original: "))
desconto = 20  # float(input("Digite a porcentagem de desconto: "))

preco_com_desconto = preco_original - (preco_original * desconto / 100)

print(
    f"Produto: {nome_produto} ->Valor: R${preco_original:.2f}\nO desconto foi de {desconto}%. \nPreço com Desconto: R$ {preco_com_desconto:.2f}"
)

print("\n3- Calculadora de Média Escolar")

nota1 = 7.5  # float(input("Digite a primeira nota: "))
nota2 = 8.0  # float(input("Digite a segunda nota: "))
nota3 = 6.5  # float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Notas: \n{nota1}, \n{nota2}, \n{nota3} \nMédia: {media:.2f}")

print("\n4- Calculadora de Consumo de Combustível")

distancia_percorrida = 300  # float(input("Digite a distância percorrida (em km): "))
combustivel_consumido = 25  # float(input("Digite o consumo de combustível (em L): "))

# Cálculo da média de consumo
media_consumo = distancia_percorrida / combustivel_consumido

print(
    f"Distancia: {distancia_percorrida} km \nConsumo de Combustível: {combustivel_consumido} L \nMédia de Consumo: {media_consumo:.2f} km/L\n"
)
