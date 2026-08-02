"""
Aim:
Convert a given integer into its Roman numeral representation.

Explanation:
Roman numerals use seven symbols: I, V, X, L, C, D, and M.
The conversion is performed from the largest value to the smallest value.
Special subtractive forms such as IV, IX, XL, XC, CD, and CM are used.

Algorithm:
1. Create a dictionary containing Roman numeral symbols and their values.
2. Arrange the values from largest to smallest, including the subtractive forms.
3. Initialize an empty result string.
4. Traverse the values from largest to smallest.
5. While the current value can be subtracted from the number, append its Roman symbol.
6. Subtract the current value from the number.
7. Continue until the number becomes 0.
8. Return the resulting Roman numeral.

Sample Input:
3749

Expected Output:
Output: MMMDCCXLIX

Time Complexity: O(n)
Space Complexity: O(1)
"""

def intToRoman(num):
    num_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""

    for value in num_map:
        while value <= num:
            result += num_map[value]
            num -= value

    return result


num = int(input("Enter an integer (1-3999): "))

print("Output:", intToRoman(num))

input("\nPress Enter to exit...")
