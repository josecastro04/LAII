'''

Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.

'''

from itertools import permutations

def multiplos(n,d):
    nums = [str(i) for i in range(1 , n + 1)]
    perm = permutations(nums)

    return sum(int(''.join(p)) % d == 0 for p in perm)