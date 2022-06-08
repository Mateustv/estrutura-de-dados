# Dado um array numbers com valores 0 e 1, nós podemos alterar K valores de 0 para 1.
# Retorne o tamanho do maior subarray contínuo que contém apenas 1.
# Exemplo 1:
# Entrada:
# numbers = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K = 2
# Saída: 6
#
# Exemplo 2:
# Entrada:
# numbers = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Saída: 10

def solution(numbers: [int], k: int):
    res = []
    test = 0
    temp = k
    second_pointer = 1
    first_pointer = 0
    while first_pointer <= len(numbers) - 1:
        if numbers[first_pointer] == 1:
            res.append(numbers[first_pointer])
            first_pointer += 1
            continue
        if numbers[first_pointer] == 0 and temp > 0:
            res.append(numbers[first_pointer])
            first_pointer += 1
            temp -= 1
            continue
        if temp == 0 or first_pointer > len(numbers) - 1:
            if len(res) > test:
                test = len(res)
            res = []
            first_pointer = second_pointer
            # print(test)
            second_pointer += 1
            temp = k
    print(test)

solution( [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)