# O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par de números que somados batam com o valor da variável target.
#
# Ele pode ser escrito em um algoritmo que roda no tempo O(n).
#
# Exemplos
# Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu programa deve retornar:
#
# [-2, 11]
#
# O motivo é bastante simples:
#
# -2 + 11 = 9

                ####################
                # RESOLUCAO O(N^2) #
                ####################

# def solution (target_sum,numbers):
#     first_poniter = len(numbers) - 1
#     array_resunt = []
#     for second_poniter in range(len(numbers)):
#         while first_poniter > second_poniter:
#             if((numbers[first_poniter] + numbers[second_poniter]) == target_sum):
#                 array_resunt.append(numbers[first_poniter])
#                 array_resunt.append(numbers[second_poniter])
#             first_poniter -= 1
#         first_poniter = len(numbers) - 1
#
#     return print(array_resunt)

                ####################
                #  RESOLUCAO O(N)  #
                ####################
def solution(target_sum, numbers):
    calc_number = {}
    for n in numbers:
        calc_test = (target_sum - n)
        if calc_test in calc_number:
            return [calc_test, n]
        else: calc_number[n] = True
    return []

solution(9,[4, 1, 2, -2, 11, 16, 1, -1, -6, -4])