#mode
#r - leitura
#a - append / incrementar
#w - escrita
#x - create file
#r+ - leitura + escrita

#arquivo = open("Aula12_Manipulando_arquivos/test2.txt","w")

#print(arquivo.readable()) #verificar se pode ser lido

#lista = arquivo.readlines() #tranforma em lista para manipular dadods
#print(lista)

#arquivo.write("Ruby\n")
#arquivo.write("C\n")
#arquivo.write("Java\n")
#arquivo.write("Pyhton\n")

#arquivo.close()

import os

# if os.path.exists("Aula12_Manipulando_arquivos/test2.txt"):
#     os.remove("Aula12_Manipulando_arquivos/test2.txt")
# else:
#     print("Arquivo não existe")

os.rmdir("Aula12_Manipulando_arquivos/nova_pasta")
