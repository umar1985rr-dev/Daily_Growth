"""
Aim:
Find the length of the longest substring without repeating characters.

Explanation:
Given a string, determine the length of the longest substring that contains
only unique characters. A sliding window and dictionary are used.

Algorithm:
1. Create an empty dictionary to store the last index of each character.
2. Initialize the left pointer (l) and maximum length to 0.
3. Traverse the string using the right pointer (r).
4. If the current character already exists within the current window, move the left pointer.
5. Update the maximum length.
6. Store the current character and its index.
7. Repeat until the end of the string.
8. Return the maximum length.

Sample Input:
abcabcbb

Expected Output:
Output: 3

Time Complexity: O(n)
Space Complexity: O(n)
"""

def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, r - l + 1)
        seen[char] = r
    return length

s = input("Enter the string: ")
print("Output:", lengthOfLongestSubstring(s))
input("\nPress Enter to exit...")
