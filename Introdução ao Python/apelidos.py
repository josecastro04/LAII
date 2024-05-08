'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    apelidos = [(nome, len(nome.split(' ')) - 1) for nome in nomes];
    apelidos.sort(key = lambda x : (x[1], x[0]));
    return [nome for nome, _ in apelidos];