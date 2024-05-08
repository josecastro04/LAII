'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    invalidos = [];
    for livro in livros:
        isbn = livros[livro];
        if len(isbn) != 13:
            invalidos.append(livro);
            continue;
        soma = 0;
        for i, n in enumerate(isbn):
            if i  % 2 == 0:
                soma += int(n);
            else:
                soma += 3 * int(n);
        if soma % 10 != 0:
            invalidos.append(livro);

    return sorted(invalidos);