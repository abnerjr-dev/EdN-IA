print("Atividade prática 3")
print("------------------------")

print("\n1- Classificador de Idades")
idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Nasça primeiro.")
elif idade <= 12:
    print("Você é criança.")
elif idade <= 17:
    print("Você é adolescente.")
elif idade <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso.")

print("\n2- Calculadora de IMC")

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (cm): ")) / 100
imc = peso / (altura**2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")

print("\n3- Conversor de Temperatura")

temp_in = input("Digite a unidade a ser convertida (C, F, K): ").upper()
temp_out = input("Digite a unidade para a qual deseja converter (C, F, K): ").upper()
temp_value = float(input("Digite o valor da temperatura: "))
converted = float("nan")

if temp_in == "C":
    if temp_out == "F":
        converted = (temp_value * 9 / 5) + 32
    elif temp_out == "K":
        converted = temp_value + 273.15
    else:
        converted = temp_value
elif temp_in == "F":
    if temp_out == "C":
        converted = (temp_value - 32) * 5 / 9
    elif temp_out == "K":
        converted = (temp_value - 32) * 5 / 9 + 273.15
    else:
        converted = temp_value
elif temp_in == "K":
    if temp_out == "C":
        converted = temp_value - 273.15
    elif temp_out == "F":
        converted = (temp_value - 273.15) * 9 / 5 + 32
    else:
        converted = temp_value
else:
    print("Unidade de temperatura inválida.")

print(f"A temperatura convertida é: {converted:.2f}{temp_out}")

print("\n4- Verificador de Ano Bissexto")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
