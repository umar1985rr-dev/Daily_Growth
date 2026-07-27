"""
Aim:
Convert a given string into a zigzag pattern based on the given number of rows and return the row-wise reading.

Explanation:
Characters are arranged in a zigzag pattern across the specified number of rows.
After reaching the last row, the direction changes upward. Finally, all rows are joined.

Algorithm:
1. Check if the number of rows is 1 or greater than or equal to the string length. If so, return the original string.
2. Create a separate list for each row.
3. Initialize the current row index and direction.
4. Traverse each character in the string.
5. Append the character to the current row.
6. Change the direction when the first or last row is reached.
7. Move to the next row based on the current direction.
8. Join all rows and return the final converted string.

Sample Input:
PAYPALISHIRING
3

Expected Output:
Output: PAHNAPLSIIGYIR

Time Complexity: O(n)
Space Complexity: O(n)
"""

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    idx, d = 0, 1
    rows = [[] for _ in range(numRows)]
    for char in s:
        rows[idx].append(char)
        if idx == 0:
            d = 1
        elif idx == numRows - 1:
            d = -1
        idx += d
    for i in range(numRows):
        rows[i] = ''.join(rows[i])
    return ''.join(rows)

s=input("Enter the string: ")
numRows=int(input("Enter the number of rows: "))
print("Output:", convert(s,numRows))
input("\nPress Enter to exit...")
