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