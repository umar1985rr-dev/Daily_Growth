"""
Aim:
Convert a string into a 32-bit signed integer following the atoi rules.

Explanation:
Ignore leading whitespace, determine the sign, read consecutive digits,
stop at the first non-digit character, and keep the result within the
32-bit signed integer range.

Algorithm:
1. Remove leading whitespace.
2. If the string is empty, return 0.
3. Determine the sign using '+' or '-'.
4. Skip leading zeros.
5. Read consecutive digits and form the integer.
6. Stop when a non-digit character is encountered.
7. Clamp the value to the 32-bit signed integer range.
8. Return the final integer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def myAtoi(s):
    s=s.lstrip()
    if not s:
        return 0
    sign=1
    i=0
    if s[0]=='-':
        sign=-1
        i+=1
    elif s[0]=='+':
        i+=1
    while i<len(s) and s[i]=='0':
        i+=1
    res=0
    found=False
    while i<len(s) and s[i].isdigit():
        found=True
        res=res*10+int(s[i])
        if sign*res>2**31-1:
            return 2**31-1
        if sign*res<-2**31:
            return -2**31
        i+=1
    if not found:
        return 0
    return sign*res

s=input("Enter the string: ")
print("Output:", myAtoi(s))
input("\nPress Enter to exit...")
