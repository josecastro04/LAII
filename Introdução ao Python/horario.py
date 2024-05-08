"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

def horario(ucs,alunos):
    a = [];

    for nAluno, cadeiras in alunos.items():
        podeAssistir = True;
        horas = 0;
        diasDaSemana = {'segunda' : 0,
                        'terca' : 0,
                        'quarta' : 0,
                        'quinta' : 0,
                        'sexta': 0};

        for cadeira in cadeiras:
            if cadeira in ucs:
                (dia, hora, duracao) = ucs[cadeira];
                if diasDaSemana[dia] == 0:
                    diasDaSemana[dia] = hora + duracao;
                    horas += duracao;
                elif diasDaSemana[dia] <= hora:
                    diasDaSemana[dia] += duracao;
                    horas += duracao;
                else:
                    podeAssistir = False;
            else:
                podeAssistir = False;

        if podeAssistir == True:
            a.append((nAluno, horas));

    a.sort(key = lambda x : (-x[1], x[0]));

    return a;

            


