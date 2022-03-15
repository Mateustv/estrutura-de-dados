# Data uma string, retorne o tamanho da maior substring
# que não tenha nenhum caracter repetido.
# Exemplo 1:
# Entrada: abcabcbb Saida: 3
# Resposta: O valor encontrado é "abc", que tem o tamanho 3.
# Exemplo 2:
# Entrada: zzzabcdzzz
# Saida: 5
# Resposta: O valor encontrado é "zabcd", que tem o tamanho 5.
#


def solution(s):
    result = 0
    for first_pointer in range(len(s)):
        hash_table = {s[first_pointer]: 'ok'}
        second_pointer = first_pointer
        while True:
            second_pointer += 1
            if (second_pointer >= len(s)) or (s[second_pointer] in hash_table):
                result = max(len(hash_table.keys()), result)
                break
            hash_table[s[second_pointer]] = 'ok'
    return print(result)


solution('zzzabcdzzz')

