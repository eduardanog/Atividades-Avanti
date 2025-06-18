#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
numeros = [7,1,6,96,55,84,72,12,100]

def segundoMaior(lista):
    if len(lista) < 2:
        print("Só existe um valor") 
    
    maior = segMaior = None
    
    for numero in lista:
        if maior is None:
            maior = numero
        elif numero > maior:
            segMaior = maior  
            maior = numero      

    return segMaior


print("Segundo maior valor:", segundoMaior(numeros))