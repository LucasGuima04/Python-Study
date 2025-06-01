minha_string = "Qualquer Texto"
print(f"concatenar {minha_string} em string")

print(minha_string.upper()) #deixar me maiuscula
print(minha_string.lower())
print(minha_string.capitalize()) #primeira letra de cada pal mais
print(minha_string.isupper()) #islower() (checar em boleano se é mais ou menos)
print(minha_string.strip()) #remover espaços
print(minha_string.replace("u","Meu",1)) #substituir

print(len(minha_string)) #tamanho da string
print(minha_string[2:7]) #escolher letra (como vetor) -> negativo = traz pra frente(começa -1)


print(minha_string.index("u")) #retorna o indice do vetor

x = "Texto" in minha_string #verificar se existe ou n na str (bool)

a = """linha1 
linha2
linha3
""" #ou \n igual em C -> \" para adicionar aspas no texto
print(a)