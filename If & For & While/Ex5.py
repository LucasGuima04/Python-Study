def soma(a,b):
    return a+b

while True:
    print("[1] Ver mensagem de boas-vindas")
    print("[2] Calcular soma de dois numeros")
    print("[3] Sair")
    validador = int(input("Escolha uma opcao!"))
    if validador == 1:
        print("\n")
        print("Seja bem-vindo ao meu programa!")
        print("\n")
    elif validador == 2:
        num1 = int(input("Insira o primeiro numero: "))
        num2 = int(input("Insira o segundo numero: "))
        print(f"A soma = {soma(num1,num2)}")
        print("\n")
    elif validador == 3:
        print("Fim!")
        break
    else:
        print("\nDigite um numero valido!")