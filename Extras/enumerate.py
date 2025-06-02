# minha_lista = ["maçã", "banana", "cereja"]
# for i in range(len(minha_lista)):
#     print(f"Índice: {i}, Fruta: {minha_lista[i]}")

# com enumerate

minha_lista = ["maçã", "banana", "cereja"]
for indice, fruta in enumerate(minha_lista):
    print(f"Índice: {indice}, Fruta: {fruta}")

#--------EXEMPLOS--------#

# nomes = ["Alice", "Bob", "Carlos"]
# for indice, nome in enumerate(nomes):
#     print(f"Pessoa {indice}: {nome}")

# tarefas = ["Lavar louça", "Varrer a casa", "Passear com o cachorro"]
# for numero_tarefa, tarefa_descricao in enumerate(tarefas, start=1):
#     print(f"Tarefa {numero_tarefa}: {tarefa_descricao}")

# palavra = "Python"
# for i, letra in enumerate(palavra):
#     print(f"No índice {i} temos a letra '{letra}'")