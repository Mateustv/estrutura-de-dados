# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 3:
#
# Input: x = 120
# Output: 21

def reverse_integer(x):
    if x >= 0:
        reverse = str(x)[::-1]
        ans = (int(reverse))
    else:
        transformer_positive = x * (-1)
        reverse = str(transformer_positive)[::-1]
        ans = (int(reverse) * (-1))
    if (ans <= -2 ** 31) or (ans >= 2 ** 31 - 1):
        return 0
    else:
        return ans

reverse_integer(120)