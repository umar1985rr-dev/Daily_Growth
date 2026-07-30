"""
Aim:
Check whether a given integer is a palindrome.

Explanation:
A palindrome number reads the same from left to right and from right to left.
Negative numbers are not palindromes because of the negative sign.

Algorithm:
1. If the number is negative, return False.
2. Store a copy of the original number.
3. Initialize the reversed number as 0.
4. Extract the last digit using the modulus operator.
5. Append the digit to the reversed number.
6. Remove the last digit from the original number.
7. Repeat until all digits are processed.
8. Compare the reversed number with the original number.
9. Return True if both are equal; otherwise, return False.

Sample Input:
121

Expected Output:
Output: True

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def isPalindrome(x):
    if x < 0:
        return False

    reverse = 0
    xcopy = x

    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10

    return reverse == xcopy

x = int(input("Enter an integer: "))
print("Output:", isPalindrome(x))

input("\nPress Enter to exit...")
