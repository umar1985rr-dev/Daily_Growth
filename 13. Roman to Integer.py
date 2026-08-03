"""
Aim:
Convert a given Roman numeral into its corresponding integer value.

Explanation:
Roman numerals use seven symbols: I, V, X, L, C, D, and M.
Most symbols are added together from left to right. In the six subtractive
cases (IV, IX, XL, XC, CD, and CM), the smaller value is placed before the
larger value and is subtracted from it. This solution replaces the subtractive
forms with their equivalent repeated symbols and then adds their values.

Algorithm:
1. Create a dictionary containing the value of each Roman numeral symbol.
2. Replace the six subtractive forms with their equivalent repeated symbols.
3. Initialize the result as 0.
4. Traverse each character in the converted Roman numeral.
5. Add the value of each character to the result.
6. Return the final integer value.

Sample Input:
MCMXCIV

Expected Output:
Output: 1994

Time Complexity: O(n)
Space Complexity: O(n)
"""

def romanToInt(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0

    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    for char in s:
        number += translations[char]

    return number

s = input("Enter a Roman numeral: ")
print("Output:", romanToInt(s))

input("\nPress Enter to exit...")
