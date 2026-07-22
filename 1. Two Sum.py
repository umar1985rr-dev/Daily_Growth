"""
LeetCode 1: Two Sum

Aim:
Find the indices of the two numbers in an array whose sum equals the target.

Problem Explanation:
Given an integer array nums and an integer target, return the indices of the
two numbers whose sum is equal to the target. Exactly one valid answer exists,
and the same element cannot be used twice.

Algorithm:
1. Create an empty dictionary.
2. Traverse the array.
3. Calculate the complement = target - current number.
4. If the complement is already in the dictionary, return the indices.
5. Otherwise, store the current number and its index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = list(map(int, input("Enter the array elements separated by space: ").replace(","," ").split()))
target = int(input("Enter the target value: "))

print("Output:", twoSum(nums, target))

input("\nPress Enter to exit...")
