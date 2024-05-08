'''
O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
'''

def salto(pontos, i, d,vis):
    i+=1;
    if d in pontos:
        return i;
    
    pontosNovos = []
    
    for ponto in pontos:
        if ponto not in vis:
            for cord in adj(ponto[0], ponto[1]):
                if cord not in vis:
                    pontosNovos.append(cord)
            vis.append(ponto)
    
    return salto(pontosNovos, i, d, vis);

def saltos(o,d):
    pontos = adj(o[0], o[1])
    i = 0
    
    if o == d:
        return 0;

    vis = []

    vis.append(o)

    return salto(pontos, i, d , vis)

def adj(x,y):
    return[(x - 1, y - 2), (x + 1, y - 2), (x - 1, y+ 2), (x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1), (x - 2, y + 1), (x -2, y -1)]