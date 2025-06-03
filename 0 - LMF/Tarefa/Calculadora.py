try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = ''

    while operador != 'stop':
        operador = input("""
[1] Soma:
[2] Subtração:
[3] Multiplicação:
[4] Divisão:
[5] Novos números:
['stop'] Finalizar\n""").replace(' ','').lower()
        if operador == 'stop':
            break
        operador = int(operador)
        
        if operador == 1:
            resultado = num1 + num2
            print(f"A soma = {resultado}\n")
        elif operador == 2:
            resultado = num1 - num2
            print(f"A subtração = {resultado}\n")
        elif operador == 3:
            resultado = num1 * num2
            print(f"A multiplicação = {resultado}\n")
        elif operador == 4:
            resultado = num1 / num2
            print(f"A divisão = {resultado}\n")
        elif operador == 5:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        else:
            print('Escolha um valor valido para a operação!')

    print("Calculadora Finalizada!")

except ZeroDivisionError:
    print("Divisão por zero não é possivel!")    
except ValueError:
    print("Digite valores validos!")
