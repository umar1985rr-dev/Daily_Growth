"""
Aim:
To find the smallest missing integer greater than the sequential prefix sum of a given list of integers.

Problem Explanation:
Given a list of integers, calculate the sequential prefix sum by adding each number to the sum if it is exactly one more than the previous number in the sequence. Once the sequence breaks, find the smallest integer greater than this sum that is not present in the list.

Algorithm:
1. Initialize `sequential_sum` with the first element of the list.
2. Iterate through the list starting from the second element to check if each number is exactly one more than the previous number.
3. If it is, add it to `sequential_sum`.
4. Once the sequence breaks, initialize `x` with `sequential_sum`.
5. Increment `x` until finding a value not present in the list.
6. Return `x`.

Time Complexity: O(n), where n is the length of the input list. The script iterates through the list once to calculate the sequential sum and then finds the smallest missing integer.

Space Complexity: O(m), where m is the number of unique elements in the input list. The space complexity is determined by the set used to store seen numbers.
"""

def missingInteger(nums):
    if not nums:
        return 1
    
    sequential_sum = nums[0]
    i = 1
    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        sequential_sum += nums[i]
        i += 1
    
    seen = set(nums)
    x = sequential_sum
    while x in seen:
        x += 1
    
    return x

nums = list(map(int, input().split()))
result = missingInteger(nums)
print(f"Output: {result}")
input("\nPress Enter to exit...")
