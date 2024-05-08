'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 
'''

def area(p,mapa):
    vis = []
    vis.append(p)

    grafo = adj(mapa)

    if mapa[p[0]][p[1]] == '*':
        return 0

    for ponto in vis:
        for p in grafo[ponto]:
            if p not in vis:
                vis.append(p)

    return len(vis)

def adj(mapa):
    d = {}

    
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == '.':
                d[(i,j)] = []
                if i-1 >= 0 and mapa[i-1][j] == '.':
                    d[(i,j)].append((i-1,j))
                if i+1 < len(mapa) and mapa[i+1][j] == '.':
                    d[(i,j)].append((i+1,j))
                if j-1 >= 0 and mapa[i][j-1] == '.':
                    d[(i,j)].append((i,j-1))
                if j+1 < len(mapa[i]) and mapa[i][j+1] == '.':
                    d[(i,j)].append((i,j+1))
    return d

        