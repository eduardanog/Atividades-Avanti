#Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
lista1=[0,2,19,8,12,13]
lista2=[0,1,2,3,8,17,13]

def elementosLista(lista1,lista2):
    lista3=[]
    for elemento in lista1:
        if elemento not in lista2 and elemento not in lista3:
            lista3.append(elemento)
    
    for elemento in lista2:
        if elemento not in lista1 and elemento not in lista3:
            lista3.append(elemento)

    return lista3

print("Elementos:\n", elementosLista(lista1, lista2))