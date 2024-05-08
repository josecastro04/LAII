'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    pos = 1
    
    max_x , max_y = 0, 0
    
    min_x, min_y = 0, 0
    
    pos_x, pos_y = 0, 0
    
    lista = []
    
    for c in comandos:
        if c == "A":
            if pos == 1:
                pos_y += 1
            elif pos == 2:
                pos_x -= 1
            elif pos == 3:
                pos_y -= 1
            else:
                pos_x += 1
        elif c == "E":
            pos += 1
        elif c == "D":
            pos -= 1
        else:
            lista.append((min_x, min_y, max_x, max_y))
            max_x , max_y = 0, 0
            min_x, min_y = 0, 0
            pos_x, pos_y = 0, 0
            pos = 1
            
        if pos > 4:
            pos = 1
        elif pos < 1:
            pos = 4
            
        if max_x < pos_x:
            max_x = pos_x
        if max_y < pos_y:
            max_y = pos_y
        if min_x > pos_x:
            min_x = pos_x
        if min_y > pos_y:
            min_y = pos_y
    
    return lista