#def nome da funcao (parametros):
    #oq vai fazer
#return oq ela vai retornar

#sao DRY(dont repeat yourself) ->evita repeticão desnecessária no codigo

def multiplicacao(a,b):
    return a*b

num1 = 15
num2 = 10

def soma(*args): #-> como tupla
    return sum(args)  #soma todos os valores passados

resultado = soma(1,2,10,30) #Passando vários argumentos
print(resultado)

#parametros kwargs->dicionarios chave valor
def exibir(**kwargs):
    for chave,valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir(nome ="Lucas", idade =20, cidade= "jundiai")

def exmplo (*args, **kwargs):
    print("Args: ", args) #Imprime os arg
