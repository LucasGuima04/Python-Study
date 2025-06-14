#são uma forma concisa e eficiente de criar listas, dicionários e conjuntos
#em uma única linha de codigo, torna mais legivel
#list, dict said comprehension

#melhora legibilidade, desempenho mais rápido, codigo mais elegante

#List Comprehension -> gerar uma lista nova com iterações ja existentes ([dado for dado in lista_base])

numeros = [1,2,3,4,5,6]
res = [numero**2 for numero in numeros if numero % 2 == 0]
#print(res)

def funcao(valor):
    return valor * valor
resp = [funcao(numero) for numero in numeros]
#print(resp)

#Listas aninhadas
listas = [[1,2,3],[4,5,6],[7,8,9]]
#print(listas[0][1]) -> saídas: 2
#for i in range(3): -> imprimir em formato de matriz
    #print(listas[i]) 

res = [[numero for numero in lista] for lista in listas]
#print(res)
#------------------------------------------------------------------------#
#Dict Comprehension
#Sintaxe: {chave: valor for chave, valor in dicionario_base}

numeros2 = {'a': 1, 'b':2, 'c': 3, 'd': 4}
res = {chave:numero *numero for chave, numero in numeros2.items() if numero % 2 == 0}
#print(res)

numeros = [1,2,3,4,5]
res = {numero: numero * numero for numero in numeros if numero % 2 == 0}
#print(res)
#------------------------------------------------------------------------#
#Set Comprehension
#Sintaxe: {dado for dado in set_base}

numeros = {1,2,3,4,5}
res = {numero*numero for numero in numeros}
#print(res)