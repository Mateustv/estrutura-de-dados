# Given a string s, return the longest palindromic substring in s
# Example 1:
#
# Input: s = "abbaaabccba"
# Output: "abccba"

def polindromic(s):
    max_polindromic = ''
    for pointer_first in range(len(s)):
        for pointer_second in range(len(s), pointer_first, -1):
            if len(max_polindromic) >= (pointer_second - pointer_first):
                print(s[pointer_first:pointer_second], pointer_second , pointer_first)
                break
            elif s[pointer_first:pointer_second] == s[pointer_first:pointer_second][::-1]:
                max_polindromic = s[pointer_first:pointer_second]
                break
    return max_polindromic

a = polindromic('abbaaabccba')
print(a)
