# Simplifique o path absoluto para um arquivo (no estilo Unix). Em outras palavras, converta o mesmo para o modo canonico.
#
# Neste modo, o '.' se refere ao diretório atual. '..' se refere ao diretório acima.
#
# Lembre-se que o path neste formato deve sempre começar com '/' e sempre devera ter um '/' único entre os diretórios.
#
# Exemplo 1:
# Entrada: "/home/"
# Saída: "/home"
#
# Exemplo 2:
# Entrada: "/home/../"
# Saída: "/"
#
# Exemplo 3:
# Entrada: "/home/../home/./"
# Saída: "/"
#
# Exemplo 4:
# Entrada: "/home/../home"
# Saída: "/home"

def solution(path):
    poiter_two = 0
    stack = []
    current = ''

    if path[-1] != '/':
        path += '/'

    for poiter_one in range(len(path)):
        if path[poiter_one] == '/':
            current = path[poiter_two:poiter_one]
            poiter_two = poiter_one

            if current:
                if current == '/..':
                    if stack:
                        stack.pop()
                elif current == '/.' or current == '/':
                    continue
                else:

                    stack.append(current)

    if not stack:
        stack.append('/')

    return ''.join(stack)
