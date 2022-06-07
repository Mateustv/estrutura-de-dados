# Dado um array que nunca é vazio, retorne os K elementos mais frequentes do mesmo.
#
# Exemplos
# Entrada: [1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10] -> K = 2
#
# Saída: [1, 3]
#
# Explicação: Os 2 números mais frequentes são 1 e 3.
def solution(numbers, k):
    hash_map = {}
    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1
    # pairs = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    # results = []
    # for pair in pairs[:k]:
    #     results.append(pair[0])
    # print(results)
    frequency = {}
    for number, count in hash_map.items():
        if count not in frequency:
            frequency[count] = []
        frequency[count].append(number)
    results = []
    for number in reversed(range(len(numbers) + 1)):
        if number in frequency:
            results.extend(frequency[number])
    print(results)

solution([1, 1, 1, 2, 2, 3, 3], 3)
