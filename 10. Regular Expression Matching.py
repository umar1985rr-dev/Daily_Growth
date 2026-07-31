"""
LeetCode 10: Regular Expression Matching

Aim:
Determine whether the entire input string matches the given pattern using '.' and '*'.

Explanation:
'.' matches any single character.
'*' matches zero or more occurrences of the preceding element.
The match must cover the entire string, not just part of it.
This solution uses recursive backtracking with memoization.

Algorithm:
1. Start from the last character of both the string and pattern.
2. Create a cache to store previously calculated index pairs.
3. If both the string and pattern are completely processed, return True.
4. If the string is finished, check whether the remaining pattern can represent an empty string.
5. If the pattern is finished while characters remain in the string, return False.
6. If the current pattern character is '*', first try matching zero occurrences of its preceding element.
7. If the preceding element matches the current string character or is '.', try consuming one string character while keeping '*' active.
8. If the current pattern character is '.' or matches the current string character, move both indices backward.
9. Store the result in the cache.
10. Return the final matching result.

Sample Input:
String: aa
Pattern: a*

Expected Output:
Output: True

Time Complexity: O(m × n)
Space Complexity: O(m × n)
"""

def isMatch(s, p):
    i, j = len(s) - 1, len(p) - 1
    return backtrack({}, s, p, i, j)

def backtrack(cache, s, p, i, j):
    key = (i, j)
    if key in cache:
        return cache[key]

    if i == -1 and j == -1:
        cache[key] = True
        return True

    if i != -1 and j == -1:
        cache[key] = False
        return False

    if i == -1 and p[j] == '*':
        k = j
        while k != -1 and p[k] == '*':
            k -= 2
        cache[key] = (k == -1)
        return cache[key]

    if i == -1 and p[j] != '*':
        cache[key] = False
        return False

    if p[j] == '*':
        if backtrack(cache, s, p, i, j - 2):
            cache[key] = True
            return True
        if p[j - 1] == s[i] or p[j - 1] == '.':
            if backtrack(cache, s, p, i - 1, j):
                cache[key] = True
                return True

    if p[j] == '.' or s[i] == p[j]:
        if backtrack(cache, s, p, i - 1, j - 1):
            cache[key] = True
            return True

    cache[key] = False
    return False

s = input("Enter the string: ")
p = input("Enter the pattern: ")

print("Output:", isMatch(s, p))

input("\nPress Enter to exit...")
