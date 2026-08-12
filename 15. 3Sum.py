"""
Aim:
To find all unique triplets in an array that sum up to zero.

Problem Explanation:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. The solution set must not contain duplicate triplets.

Algorithm:
1. Sort the array to facilitate the two-pointer technique.
2. Iterate through the array, treating each element as a potential first element of a triplet.
3. Use two pointers (left and right) to find pairs that sum up with the current element to zero.
4. Skip duplicates for both the current element and the elements at the left and right pointers.

Time Complexity: O(n^2)
Space Complexity: O(1), excluding the space required for the output
"""

def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = threeSum(nums)
print(f"Output: {result}")
input("\nPress Enter to exit...")
