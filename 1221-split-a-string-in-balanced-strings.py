'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''

def balancedStringSplit(s: str) -> int:
    r = 0
    l = 0
    groups = 0
    for element in s:
        if element == "L":
            l += 1
        elif element == "R":
            r += 1
        if r == l:
            groups += 1
            r = 0
            l = 0
    return groups

print(balancedStringSplit("RLRRLLRLRL"))




