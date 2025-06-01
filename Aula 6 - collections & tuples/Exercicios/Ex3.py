nomes = [
    "Ana", "Carlos", "Juliana", "Rafael", "Beatriz",
    "Lucas", "Mariana", "Gustavo", "Fernanda", "Pedro",
    "Camila", "João", "Larissa", "Eduardo", "Patrícia",
    "Felipe", "Renata", "André", "Tatiane", "Bruno",
    "Gabriela", "Rodrigo", "Natália", "Vinícius", "Letícia"
]
nome = input("Qual nome procurado: ").strip()

if nome in nomes:
    print("Encontrado!")
else:
    print("Nao encontrado!")