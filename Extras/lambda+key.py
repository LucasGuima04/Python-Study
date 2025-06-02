pessoas = [("Alice", 30), ("Bob", 25), ("Carlos", 35)]

# A função lambda 'lambda pessoa_tupla: pessoa_tupla[1]' faz o mesmo que 'obter_idade'
pessoas_ordenadas_por_idade = sorted(pessoas, key=lambda pessoa_tupla: pessoa_tupla[1])
print(pessoas_ordenadas_por_idade)

#---------------------------------------------------------------------------------------------------------------------#

palavras = ["banana", "maçã", "kiwi", "abacaxi"]
palavras_ordenadas_por_tamanho = sorted(palavras, key=lambda palavra: len(palavra))
print(palavras_ordenadas_por_tamanho)
# Saída: ['kiwi', 'maçã', 'banana', 'abacaxi']

#---------------------------------------------------------------------------------------------------------------------#

carros = [
    {'marca': 'Ford', 'modelo': 'Fiesta', 'ano': 2020},
    {'marca': 'Chevrolet', 'modelo': 'Onix', 'ano': 2022},
    {'marca': 'Fiat', 'modelo': 'Mobi', 'ano': 2019}
]
carros_ordenados_por_ano = sorted(carros, key=lambda carro: carro['ano'])
print(carros_ordenados_por_ano)
# Saída:
# [{'marca': 'Fiat', 'modelo': 'Mobi', 'ano': 2019},
#  {'marca': 'Ford', 'modelo': 'Fiesta', 'ano': 2020},
#  {'marca': 'Chevrolet', 'modelo': 'Onix', 'ano': 2022}]

#---------------------------------------------------------------------------------------------------------------------#

produtos = [
    {'nome': 'Caneta', 'preco': 2.50},
    {'nome': 'Caderno', 'preco': 15.00},
    {'nome': 'Borracha', 'preco': 1.00}
]
produto_mais_caro = max(produtos, key=lambda produto: produto['preco'])
print(produto_mais_caro)
# Saída: {'nome': 'Caderno', 'preco': 15.0}