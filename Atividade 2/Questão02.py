#Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes. 
numeros=[3,4,5,11,13,27,89,99,157]
primos = []

def numerosPrimos(lista):
    for numero in lista:
        if numero > 1:
            primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break
            if primo: 
                primos.append(numero)
    print("Números primos:\n",primos)

numerosPrimos(numeros)