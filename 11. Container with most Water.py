"""
Aim:
Find two vertical lines that form a container capable of storing the maximum amount of water.

Explanation:
The area of water depends on the distance between the two lines and the shorter
of their heights. A two-pointer approach starts from both ends and moves inward.

Algorithm:
1. Initialize left at the beginning and right at the end of the array.
2. Initialize max_area to 0.
3. Calculate the current area using the distance and the shorter height.
4. Update max_area if the current area is larger.
5. If the left height is smaller, move the left pointer one step right.
6. Otherwise, move the right pointer one step left.
7. Repeat while left is less than right.
8. Return the maximum area.

Sample Input:
1 8 6 2 5 4 8 3 7

Expected Output:
Output: 49

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        max_area = max(
            max_area,
            (right - left) * min(height[left], height[right])
        )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


height = list(map(int, input(
    "Enter the heights (space separated): "
).replace(",", " ").split()))

print("Output:", maxArea(height))

input("\nPress Enter to exit...")
