#Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares. 
numeros=[2,4,5,11,13,56,99,157]
resultado=[]

def numImpar(lista):
    for numero in lista:
        if numero % 2 != 0:
            resultado.append(numero)
    print("Números ímpares da lista:\n", resultado)

numImpar(numeros)