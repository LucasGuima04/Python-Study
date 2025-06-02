pessoas = [("Alice", 30), ("Bob", 25), ("Carlos", 35)]

# Função para obter a idade (o segundo elemento)
def obter_idade(pessoa_tupla):
  return pessoa_tupla[1] # Retorna o segundo elemento (índice 1)

# Função para obter o nome 1 elemento)
def obter_nome(pessoa_tupla):
  return pessoa_tupla[0] # Retorna o primeiro elemento (índice 0)

pessoas_ordenadas_por_idade = sorted(pessoas, key=obter_idade)
print(pessoas_ordenadas_por_idade)