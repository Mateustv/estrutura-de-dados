# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def intToRoman(num: int):
    symbol = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    numbers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    index = 0
    res = ''
    while num > 0:
        temp = num // numbers[index]
        if temp > 0:
            num -= numbers[index] * temp
            res += symbol[index] * temp
        index += 1
    print(res)
intToRoman(3944)