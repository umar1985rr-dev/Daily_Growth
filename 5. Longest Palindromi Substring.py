"""
Aim:
Find the longest palindromic substring in a given string using Dynamic Programming.

Explanation:
A palindrome reads the same forward and backward. This solution uses a DP table to determine whether each substring is a palindrome and keeps track of the longest one.

Algorithm:
1. Create a 2D DP table initialized to False.
2. Mark every single character as a palindrome.
3. Assume the first character is the longest palindrome.
4. Traverse all possible ending indices.
5. For each ending index, check all starting indices before it.
6. If the characters match and the inner substring is a palindrome (or the substring length is 2), mark it as a palindrome.
7. Update the longest palindrome whenever a longer one is found.
8. Return the longest palindromic substring.

Sample Input:
babad

Expected Output:
Output: bab

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

def longestPalindrome(s):
    if not s:
        return ""
    dp=[[False]*len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i]=True
    ans=s[0]
    for j in range(len(s)):
        for i in range(j):
            if s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j]=True
                if j-i+1>len(ans):
                    ans=s[i:j+1]
    return ans

s=input("Enter the string: ")
print("Output:", longestPalindrome(s))
input("\nPress Enter to exit...")
