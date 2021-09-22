# Dada uma string codificada, retorne a string decodificada.
#
# A regra de codificação é: k[string_codificada], onde a string_codificada dentro dos colchetes serão repetidas o número de k vezes. O valor de k será sempre um número positivo.
#
# Você deve assumir que as strings de entrada são sempre válidas, sem espaço e os colchetes estão bem formatados.
#
# Exemplos:
# s = "2[a]3[bc]", retornará "aabcbcbc".
# s = "3[a2[c]]", retornará "accaccacc".
# s = "2[abc]3[cd]ef", retornará "abcabccdcdcdef".


def solution(str_to_decode):
    stack = []
    temp_string = ''
    number = 0

    for s in str_to_decode:
        if s == '[':
            if temp_string:
                stack.append(temp_string)
                temp_string = ''
            stack.append(number)
            number = 0

        elif s == ']':
            if temp_string:
                stack.append(temp_string)
                temp_string = ''
            new_str = ''
            first = stack.pop()
            while first and type(first) != int:
                new_str = first + new_str
                first = stack.pop()
            new_str *= first
            stack.append(new_str)
        else:
            if s.isdigit():
                number = 10*number + int(s)
            else:
                temp_string += s
    if temp_string:
        stack.append(temp_string)
    return ''.join(stack)
