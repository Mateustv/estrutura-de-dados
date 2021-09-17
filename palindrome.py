# def solution(string):
#     # reverseString = string[::-1]
#     reverse_string = ''
#     for index in reversed(range(len(string))):
#         reverse_string += string[index]
#
#     return string == reverse_string

def solution (string):
    pointer_string = (len(string) - 1)
    for index in range(len(string)):
        if(index == pointer_string):
            return True
        if(string[index] != string[pointer_string]):
            return False
        pointer_string -= 1
    return True

mateus = solution('abba')
print(mateus)