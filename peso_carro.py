N, F, P = [int(x) for x in input().split()]
list = list(map(int, input("Enter a multiple value: ").split()))
print(list)
tempo = 0
i = 0
if F > 1:
    cont = 1
    while list:
        if cont == 1:
            if list[i] > P:
                list[i] -= 2
                tempo += 10
                cont += 1
            else:
                list.pop(i)
                N -= 1
                tempo += 5
                cont += 1
        elif cont > F:
            cont = 1
        else:
            list.pop(i)
            cont += 1
            N -= 1
            tempo += 1

        i += 1
        if i >= N:
            i = 0
else:
    while list:
        if list[i] > P:
            list[i] -= 2
            tempo += 10
        else:
            list.pop(i)
            N -= 1
            i = 0
            tempo += 5
            continue
        i += 1
        if i >= N:
            i = 0
print(tempo)

# passa_carro(4, 2, 2, [2,6,3,1])