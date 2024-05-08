'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def dfs(adj,o):
    grafo = dfs_aux(adj,o,set(),{})
    
    i = 1;
    for _ in grafo:
        i += 1
        
    return i;

def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return pai

def maior(vizinhos):
    grafo = constr(vizinhos)
    tamanho = 0
    for pais in grafo:
        t =  dfs(grafo, pais)
        if tamanho < t:
            tamanho = t
            
    return tamanho;
        
    
    
def constr(vizinhos):
    caminhos = {}
    
    for fronteiras in vizinhos:
        for paises in fronteiras:
            if paises not in caminhos:
                caminhos[paises] = set()
                
            for paises2 in fronteiras:
                if paises2 != paises:
                    caminhos[paises].add(paises2)
            
    return caminhos;