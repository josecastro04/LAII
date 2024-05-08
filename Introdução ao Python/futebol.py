'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

def tabela(jogos):
    equipas = [];
    for casa,_, fora,_ in jogos:
        equipas.append(casa);
        equipas.append(fora);
    equipas = set(equipas);

    classificacao = {equipa: [0, 0, 0 , 0] for equipa in equipas};

    for casa, golosC, fora, golosF in jogos:
        if golosC > golosF:
            classificacao[casa][0] += 3;
        elif golosC == golosF:
            classificacao[casa][0] += 1;
            classificacao[fora][0] += 1;
        else:
            classificacao[fora][0] += 3;

        classificacao[casa][1] += golosC;
        classificacao[casa][2] += golosF;
        classificacao[fora][1] += golosF;
        classificacao[fora][2] += golosC;
    
    for equipa in classificacao:
        classificacao[equipa][3] = classificacao[equipa][1] - classificacao[equipa][2];

    classificacao = sorted(classificacao.items(), key=lambda x: (-x[1][0], -x[1][3], x[0]));
    return [(equipa, pontos) for equipa, (pontos, _, _,_) in classificacao];