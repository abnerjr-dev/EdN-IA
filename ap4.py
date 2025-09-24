print("\nAtividade prática 4")
print("------------------------")

print("Calculadora Simples")

print("Vamo Calcular, maninho!")
print("\nEscolha uma das opções abaixo:")
print("+ -> Somar")
print("- -> Subtrair")
print("* -> Multiplicar")
print("/ -> Dividir")

continuar = "s"
while continuar == "s":
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == "+":
        print("Você escolheu somar!")
    elif operacao == "-":
        print("Você escolheu subtrair!")
    elif operacao == "*":
        print("Você escolheu multiplicar!")
    elif operacao == "/":
        print("Você escolheu dividir!")
    else:
        print("Operação inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
        continue

    try:
        if operacao == "+":
            resultado = num1 + num2
            print("O resultado da soma é:", resultado)
        elif operacao == "-":
            resultado = num1 - num2
            print("O resultado da subtração é:", resultado)
        elif operacao == "*":
            resultado = num1 * num2
            print("O resultado da multiplicação é:", resultado)
        elif operacao == "/":
            resultado = num1 / num2
            print("O resultado da divisão é:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
print("Valeu, até a próxima!")

print("\n2- Media da turma")

notas = []
num_alunos = int(input("Digite o número de alunos na turma: "))
for i in range(num_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas) if notas else 0
print(f"A média da turma é: {media:.2f}")

print("4- Verificador de senha")
senha = input("Digite uma senha: ")
if (
    len(senha) >= 8
    and any(c.islower() for c in senha)
    and any(c.isupper() for c in senha)
    and any(c.isdigit() for c in senha)
    and any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in senha)
):
    print("\nTa top.")
else:
    print(
        "\nhhhmmmmm.... Melhor não ein...\nA senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais."
    )

print("\n5- par ou ímpar")


continuar = "s"
num_pares = 0
num_impares = 0
while continuar == "s":
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        continue
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
        num_pares += 1
    else:
        print(f"O número {numero} é ímpar.")
        num_impares += 1
    print(f"Números pares digitados até agora: {num_pares}")
    print(f"Números ímpares digitados até agora: {num_impares}")

    continuar = input("Deseja verificar outro número? (s/n): ").lower()

    while continuar not in ["s", "n"]:
        continuar = input(
            "Por favor, responda com 's' para sim ou 'n' para não: "
        ).lower()
        if continuar == "n":
            break

print("Valeu, até a próxima atividade!")
