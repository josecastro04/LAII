'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist

def viagem(rotas,o,d):
    
    if o == d:
        return 0;
    
    grafo = adj(rotas)
    
    custo = dijkstra(grafo, o)
    
    return custo[d]
    
    
def adj(rotas):
    d =  {}
    custo = 0
    origem = "";
    for rota in rotas:
        for i, v in enumerate(rota):
            if i % 2 == 0:
                if v not in d:
                    d[v] = {}
                    if i != 0:
                        d[v][origem] = custo
                        d[origem][v] = custo
                else:
                    if i == 0:
                        origem = v
                    elif origem not in d[v]:
                        d[v][origem] = custo
                        d[origem][v] = custo
                    elif d[v][origem] > custo:
                        d[v][origem] = custo
                        d[origem][v] = custo
                
                origem = v
            else:
                custo = v
        
        
    return d