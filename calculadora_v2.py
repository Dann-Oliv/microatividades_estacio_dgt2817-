saida = ""


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num1 == 0 or num2 == 0:
        return "Não foi possível realizar a divisão por zero"
    else:
        return num1 / num2


def calculadora(num1, num2, operacao):
    if operacao == "adicao" or operacao == "+":
        resultado = adicao(num1, num2)

    elif operacao == "subtracao" or operacao == "-":
        resultado = subtracao(num1, num2)

    elif operacao == "multiplicacao" or operacao == "*":
        resultado = multiplicacao(num1, num2)

    elif operacao == "divisao" or operacao == "/":
        resultado = divisao(num1, num2)
    else:
        return "A operação não é válida"

    return resultado


while saida.lower() != "n":
    num1: float = float(input("Digite o primero número: "))
    num2: float = float(input("Digite o segundo número: "))
    operacao = input("Informe a operação desejada: ")

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar a execução?(S/N)\n")

    if saida.lower() == "n":
        print("Encerrando o programa...")
        break
