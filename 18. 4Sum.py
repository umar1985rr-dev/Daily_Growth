"""
Aim:
To solve the 4Sum problem on LeetCode, which requires finding all unique quadruplets in an array that sum up to a given target.

Problem Explanation:
Given an array of integers and a target integer, the task is to find all unique quadruplets in the array which gives the sum of the target. The solution should not contain duplicate quadruplets.

Algorithm:
1. Sort the input array to facilitate the two-pointer technique.
2. Use a nested loop to fix the first two elements of the quadruplet.
3. For each pair of fixed elements, use two pointers to find the other two elements such that their sum equals the target minus the sum of the fixed elements.
4. Skip duplicate elements to avoid duplicate quadruplets.
5. Collect all valid quadruplets and return them.

Time Complexity: O(n^3)
Space Complexity: O(1) (excluding the space required for the output)
"""

def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left, right = j+1, n-1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result

nums = list(map(int, input("Enter nums separated by space: ").split()))
target = int(input("Enter target: "))
result = fourSum(nums, target)
print(f"Output: {result}")
input("\nPress Enter to exit...")
