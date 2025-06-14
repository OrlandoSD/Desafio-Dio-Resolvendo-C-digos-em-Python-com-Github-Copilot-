# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
print("Escolha a operação matemática:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = input("Digite o número da operação: ")

# Realiza a operação escolhida
if op == '1':
    resultado = num1 + num2
    operacao = "soma"
elif op == '2':
    resultado = num1 - num2
    operacao = "subtração"
elif op == '3':
    resultado = num1 * num2
    operacao = "multiplicação"
elif op == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: divisão por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()

print(f"O resultado da {operacao} é: {resultado}")