numberses = [12, 3, 1, 2, -6, 5, -8, 6]
targate = 0


# o(n^3)
# def solution(numbers, targete):
#     result = []
#     for x in range(len(numbers)-2):
#         first = numbers[x]
#         for y in range(x+1,len(numbers) - 1):
#             second = numbers[y]
#             for z in range(y+1, len(numbers)):
#                 third = numbers[z]
#                 if first + second + third == targete:
#                     result.append(sorted([first,second,third]))
#     return result
# o(n^2)

def solution(numbers, target_number):
    result = []
    numbers_sorted = list(sorted(numbers))

    for current in range(len(numbers)):
        left_pointer = current + 1
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            sum_numbers = numbers_sorted[current]
            sum_numbers += numbers_sorted[left_pointer]
            sum_numbers += numbers_sorted[right_pointer]

            if sum_numbers > target_number:
                right_pointer -= 1
            elif sum_numbers < target_number:
                left_pointer += 1
            else:
                result.append(sorted([numbers_sorted[current], numbers_sorted[left_pointer], numbers_sorted[right_pointer]]))
                right_pointer -= 1
                left_pointer += 1

    return result


soma = solution(numberses, targate)
print(soma)
