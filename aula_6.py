print("1- Programa de Saudação")
print("Olá, mundo!")

print("2- Calculadora de Soma")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"A soma de {num1} + {num2} = {num1 + num2}.")

print("3- Calculadora de Volume")
c = 12  # float(input("Digite o comprimento: "))
l = 14  # float(input("Digite a largura: "))
a = 20  # float(input("Digite a altura: "))
Volume = c * l * a
print("O volume é:", Volume, "cm³")

print("4- Calculadora de Preço Total")

nome_produto = "Cadeira Infantil"  # input("Digite o nome do produto: ")
preco_unitario = 12.40  # float(input("Digite o preço unitário: "))
quantidade = 3  # int(input("Digite a quantidade: "))
preco_total = preco_unitario * quantidade
print(
    f"Você comprou {quantidade} unidades de {nome_produto}, O preço total é: R$ {preco_total:.2f}"
)

