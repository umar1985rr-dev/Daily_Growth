"""
Aim:
To generate all possible letter combinations that can be formed by pressing the digits of a given phone number.

Problem Explanation:
Given a string containing digits from 2 to 9 inclusive, return all possible letter combinations that can be made using those digits on a standard telephone keypad. Each digit is mapped to a set of letters (e.g., '2' -> 'abc', '3' -> 'def'). The order of the output does not matter.

Algorithm:
1. Create a dictionary mapping each digit to its corresponding letters.
2. Define a helper function `backtrack` that takes an index and a current path of letters.
3. If the index equals the length of the digits string, append the current path to the result list.
4. Otherwise, for each letter in the set mapped to the current digit, add it to the path, recursively call `backtrack` with the next index, and then remove the last letter from the path (backtracking).
5. Initialize an empty list `result` and start the backtracking process with index 0 and an empty path.
6. Return the result list containing all possible combinations.

Time Complexity: O(4^n), where n is the number of digits in the input string. In the worst case, each digit can map to 4 letters, leading to a branching factor of 4 at each level of recursion.

Space Complexity: O(n), where n is the number of digits in the input string. This space is used for the recursion stack and the current path.
"""

def letterCombinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        for letter in phone_map[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

digits = input("Enter digits: ")
print(f"Output: {letterCombinations(digits)}")
input("\nPress Enter to exit...")
