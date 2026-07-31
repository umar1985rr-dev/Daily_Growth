"""
Aim:
Reverse the digits of a given integer while ensuring the result remains within the 32-bit signed integer range.

Explanation:
Given an integer, reverse its digits. If the reversed integer exceeds the 32-bit signed integer limit, return 0.

Algorithm:
1. Determine the sign of the integer.
2. Convert the integer to its absolute value.
3. Initialize the reversed number as 0.
4. Extract the last digit using the modulus operator.
5. Append the digit to the reversed number.
6. Remove the last digit from the original number.
7. Restore the original sign.
8. Check whether the reversed number is within the 32-bit signed integer range.
9. If it exceeds the range, return 0.
10. Otherwise, return the reversed integer.

Sample Input:
123

Expected Output:
Output: 321

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10
    rev *= sign
    if rev < -(2 ** 31) or rev > 2 ** 31 - 1:
        return 0
    return rev

x = int(input("Enter an integer: "))
print("Output:", reverse(x))

input("\nPress Enter to exit...")
