"""
Aim:
Convert a given string into a 32-bit signed integer by following the rules of the atoi() function.

Explanation:
The string is first stripped of leading and trailing spaces. An optional '+' or '-' sign is processed, followed by consecutive numeric characters. Parsing stops when a non-digit character is encountered. If the value exceeds the 32-bit signed integer range, the appropriate limit is returned.

Algorithm:
1. Remove leading and trailing spaces from the string.
2. If the string is empty, return 0.
3. Initialize the sign, index, and result.
4. Check for an optional '+' or '-' sign.
5. Traverse the string while the current character is a digit.
6. Build the integer by multiplying the current result by 10 and adding the new digit.
7. Check for overflow after every digit.
8. Return the maximum or minimum 32-bit integer if overflow occurs.
9. Return the final integer with its sign.

Sample Input:
42

Expected Output:
Output: 42

Time Complexity: O(n)
Space Complexity: O(1)
"""

def myAtoi(s):
    s=s.strip()
    if not s:
        return 0
    sign,i,res=1,0,0
    if s[0]=='-':
        sign=-1
        i+=1
    elif s[0]=='+':
        i+=1
    while i<len(s) and s[i].isdigit():
        res=res*10+int(s[i])
        if sign*res>2**31-1:
            return 2**31-1
        if sign*res<-2**31:
            return -2**31
        i+=1
    return sign*res

s=input("Enter the string: ")
print("Output:", myAtoi(s))
input("\nPress Enter to exit...")
