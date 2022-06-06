# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 2:
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

def isMatch(s:str, p:str) -> bool:
    match = {}
    second_pointer = 0
    for first_pointer in range(len(s)):
        if s[first_pointer] == p[second_pointer] or p[first_pointer] == '.':
            print('ok')

        second_pointer += 1

isMatch('aaa', 'a..')

