"""
Aim:
To find the longest common prefix (LCP) among an array of strings.

Problem Explanation:
Given an array of strings, write a function to return the longest string that is a prefix of all the strings in the array. If there is no common prefix, return an empty string.

Algorithm:
1. Initialize the prefix with the first string in the array.
2. Iterate through the rest of the strings in the array.
3. For each string, use a while loop to reduce the prefix from the end until it becomes a prefix of the current string or becomes an empty string.
4. If at any point the prefix becomes an empty string, return an empty string immediately as there can't be a common prefix.
5. After iterating through all strings, return the final prefix.

Time Complexity: O(S), where S is the total number of characters in all strings combined.
Space Complexity: O(1), as we are using a constant amount of extra space.
"""

def longestCommonPrefix(strs):
    if not strs: return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix: return ""
    return prefix

strs = input().split(',')
result = longestCommonPrefix(strs)
print(f"Output: {result}")
input("\nPress Enter to exit...")
