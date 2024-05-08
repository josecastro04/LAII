'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
'''

def caminhoMaisCurto(caminhos, fim):
    pai = {}

    visitados = {(0,0)}

    fila = []
    fila.append((0,0))

    while fila:
        ponto = fila.pop(0)
        for p in caminhos[ponto]:
            if p not in visitados:
                visitados.add(p)
                pai[p] = ponto
                fila.append(p)

    ponto = fim

    string = ""

    while ponto != (0,0):
        (x,y) = ponto
        p = pai[ponto]
        (x1,y1) = p
        if x < x1 :
            string += "S"
        elif x > x1:
            string += "N"
        elif y < y1:
            string += "O"
        elif y > y1:
            string += "E"


    return string[::-1]


def caminho(mapa):

    destino = len(mapa) -2 

    caminhos = adj(mapa, destino)

    return caminhoMaisCurto(caminhos, (destino,destino))


def adj(mapa, mapaLen):
    grafo = {}
    for index in range(mapaLen):
        for indey in range(mapaLen):
            if (index, indey) not in grafo and mapa[index][indey] != '#':
                grafo[(index, indey)] = set()
            
                if index > 0 and mapa[index - 1][indey] == ' ':
                    grafo[(index, indey)].add((index-1, indey))

                if index < mapaLen - 1 and mapa[index + 1][indey] == ' ':
                    grafo[(index, indey)].add((index+1, indey))

                if indey > 0 and mapa[index][indey - 1] == ' ':
                    grafo[(index, indey)].add((index, indey-1))

                if indey < mapaLen - 1 and mapa[index][indey + 1] == ' ':
                    grafo[(index, indey)].add((index, indey+1))

    return grafo;
