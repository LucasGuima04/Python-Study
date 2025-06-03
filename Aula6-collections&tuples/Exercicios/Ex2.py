
lista = []
print("Insira 5 numeros: ")

for itens in range(5):
    a = int(input())
    lista.append(a)

print(f"{lista.sort()}")
print(f"O maior numero: {max(lista)}")
print(f"O menor numero: {min(lista)}")
print(f"A media da lista: {sum(lista)/len(lista)}")

