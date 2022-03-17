# The string "PAYPALISHIRING" is written in a zigzag pattern on a given
# number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

def zigzag(s , nubLine):
    answer = ''
    if nubLine <= 1:
        return s
    for row in range(nubLine):
        jump = (nubLine - 1) * 2
        for letter in range(row, len(s),jump):
            answer += s[letter]
            if row != 0 and row != nubLine - 1 and (letter + jump - 2 * row) < len(s):
                answer += s[letter + jump - row * 2]
    return answer

a = zigzag('PAYPALISHIRING', 4)
print(a)

