"""
Aim:
To find the sum of three integers in an array that is closest to a given target.

Problem Explanation:
Given an array nums of n integers and an integer target, return the sum of the three integers such that the sum is closest to target.
The solution should return the closest sum found. If there are multiple answers, any one of them is acceptable.

Algorithm:
1. Sort the input array nums.
2. Initialize a variable closest_sum with infinity to store the closest sum found so far.
3. Iterate through the array using a for loop, considering each element as the first element of the triplet.
4. For each first element, use two pointers (left and right) to find the other two elements such that their sum is closest to the target.
5. If the current sum is less than the target, move the left pointer to the right to increase the sum.
6. If the current sum is greater than the target, move the right pointer to the left to decrease the sum.
7. If the current sum equals the target, return it immediately as it's the closest possible sum.
8. After iterating through all elements and adjusting pointers, return the closest_sum found.

Time Complexity: O(n^2), where n is the number of elements in the input array nums. The sorting step takes O(n log n), and the nested while loop iterates over each element once.

Space Complexity: O(1), as no additional space proportional to the input size is used.
"""

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    
    return closest_sum

nums = list(map(int, input("Enter nums separated by space: ").split()))
target = int(input("Enter target: "))
result = threeSumClosest(nums, target)
print(f"Output: {result}")
input("\nPress Enter to exit...")
