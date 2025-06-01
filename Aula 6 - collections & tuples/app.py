familia = ["Lucas","Matheus","Joao","Odete"]

#print(familia[0])
#print(familia[-1])
#print(familia[1:3])

#print(familia)
familia[3] = "Adoberval"
#print(familia)

familia.extend(["Amaro","Damiana","Alice","Joao BG"])#add varios valores(final)
familia.append("Jorge") #add um valor(final)
familia.insert(2,"Bidu") #entra no lugar do indice 2 e joga os outros pra frente

familia.pop() #remove o ultimo valor
familia.remove("Bidu") #remove o especico valor
familia.clear() #limpar lista

familia.index("Lucas")

idade_familia = [20,26,60,54]
idade_familia.sort() #ordena numeros
familia.sort() #ordem alfabetica
print(idade_familia)
print(familia)

idade_familia.reverse() #inverte a lista

familia2 = familia
familia.remove("Lucas")
print(familia2)

coordenadas = (-49,-36) #-> tuple (Lista Imutavel)
coordenadas.count(-49) #contagem de itens

