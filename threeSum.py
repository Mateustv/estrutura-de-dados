# O Three sum é uma variação do problema Two Sum, caso você ainda não tenha feito ele sugiro que vá primeiro nele e depois volte aqui.
#
# A idéia deste problema é identificar todos os três números que quando somados resultem em um valor especificado.
#
# Exemplos
# Se o array é [12, 3, 1, 2, -6, 5, -8, 6] e o target é 0. Neste caso, seu programa deve retornar:
#
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]
#
# A soma de todos os valores das listas acima será igual a zero.

def solution(numbers, target_sum):
    second_pointer = len(numbers) - 1
    three_pointer = len(numbers) -1
    array_test = []

    for first_pointer in numbers:
        while numbers[second_pointer] != first_pointer:
            value_intermd = first_pointer + numbers[second_pointer]
            while numbers[three_pointer] != first_pointer :
                three_pointer -= 1
                if((value_intermd + numbers[three_pointer]) == target_sum):
                    array_test.append([first_pointer, numbers[second_pointer],numbers[three_pointer]])
            # second_pointer -= 1
        three_pointer = len(numbers)-1
    return print(array_test)
solution([12, 3, 1, 2, -6, 5, -8, 6],0)