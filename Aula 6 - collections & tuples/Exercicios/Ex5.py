entrada = input("Digite números separados por vírgula (ex: 1,2,3,4): ")

# Passo 1: Dividir a string em partes
partes = entrada.split(",")  # retorna uma lista de strings

# Passo 2: Converter cada parte para inteiro
numeros_lista = [int(p.strip()) for p in partes]

# Passo 3: Converter a lista em tupla
numeros_tupla = tuple(numeros_lista)

# Passo 4: Mostrar os resultados
print("Lista:", numeros_lista)
print("Tupla:", numeros_tupla)