"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    numberAlunos = list(prefs.keys());
    numberAlunos.sort();

    projetos = {};

    for aluno in numberAlunos:
        for projeto in prefs[aluno]:
            if projeto not in projetos:
                projetos[projeto] = aluno;
                break;

    return [aluno for aluno in numberAlunos if aluno not in projetos.values()];
