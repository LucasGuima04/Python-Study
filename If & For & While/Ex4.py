
while True:
    num = int(input("Insira sua idade: "))
    if num > 0 and num < 120:
        break
    else:
        print("Insira um numero valido 0 < Idade < 120")
    
print(f"Sua idade e {num} ")