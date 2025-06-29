#sintaxe: map(funcão,iteravel1,iteravel2)

#para visualizar converter para lista
#aplica a função elemento por elemento
#mais eficiente em list comprehension

def quadrado(x):
    return x**2

numeros = [1,2,3,4,5]

#jeito 1
res = map(quadrado,numeros)
print(list(res))

#jeito 2
res = list(map(lambda x,y:quadrado(x)+ y,numeros,numeros))
print(res)