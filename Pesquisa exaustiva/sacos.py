'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

'''

def complete(lista, compras):
    return len(lista) == len(compras)

def valid(lista, compras, peso, sacos):
    soma = 0
    s = 1
    for i, p in enumerate(lista):
        soma += compras[p]
        
        if i < len(lista) - 1 and soma + compras[lista[i + 1]] > peso:
            soma = 0
            s+=1
        
        if s > sacos:
            return False
    
    return s == sacos
def aux(peso,compras,lista, sacos):
    if complete(lista, compras):
        return valid(lista, compras, peso, sacos)
        
    for i in range(len(compras)):
        if i in lista:
            continue
        lista.append(i)
        if aux(peso, compras, lista, sacos):
            return True
        
        lista.pop()
    return False;
    
def sacos(peso,compras):
    lista = []
    sacos = 1
    if peso == 0:
        return 0
    while(not aux(peso, compras, lista, sacos)):
        sacos += 1
        
    return sacos