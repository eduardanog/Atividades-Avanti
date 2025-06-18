#Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
informacoes=[("Fernanda",27),("Eduarda", 21), ("Antonio",28),("Marta",25), ("Maria", 16)]

def ordemAlfa(lista):
    return sorted(lista) 

print("Lista ordenada:\n", ordemAlfa(informacoes))

