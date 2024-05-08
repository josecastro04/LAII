'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    subStrings = texto.split(" ");
    freq = [(string, subStrings.count(string)) for string in subStrings];
    freq = list(set(freq));
    freq.sort(key = lambda x : (-x[1],x[0]));
    return [string for (string, _) in freq];