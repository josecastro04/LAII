"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def checkCard(number, newNumber):
    n = "";

    for i, num in enumerate(number):
        if (n == "*" and newNumber[i] != "*") or (n != "*" and newNumber[i] != "*"):
            n += newNumber[i];
        else:
            n += num;
        
    return n;
    
    
def contaN(number):
    acc = 0;
    for c in number:
        if c != "*":
            acc += 1;
    
    return acc;

def hacker(log):
    newLogs = {}
    
    for c, email in log:
        if email not in newLogs:
            newLogs[email] = c;
        else:
            newLogs[email] = checkCard(newLogs[email], c);
            
            
    for email in newLogs:
        newLogs[email] = (newLogs[email], contaN(newLogs[email]))
    
    lista = list(newLogs.items())
    lista.sort(key = lambda x : (-x[1][1], x[0]))

    lista = [(conta, email) for email, (conta, acc) in lista]

    return lista;