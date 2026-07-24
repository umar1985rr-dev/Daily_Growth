"""
Aim:
Find the median of two sorted arrays by merging them into a single sorted array.

Explanation:
Given two sorted arrays, merge them into one sorted array and find the median.
If the total number of elements is odd, the median is the middle element.
If the total number of elements is even, the median is the average of the two middle elements.

Algorithm:
1. Merge the two sorted arrays into a single array.
2. Sort the merged array.
3. Find the total number of elements.
4. If the total number of elements is odd, return the middle element.
5. If the total number of elements is even, find the two middle elements.
6. Calculate the average of the two middle elements.
7. Return the median.

Sample Input:
First array: 1 3
Second array: 2

Expected Output:
Output: 2.0

Time Complexity: O((n + m) log(n + m))
Space Complexity: O(n + m)
"""

def findMedianSortedArrays(nums1, nums2):
    merged = nums1 + nums2
    merged.sort()
    total = len(merged)
    if total % 2 == 1:
        return float(merged[total // 2])
    else:
        middle1 = merged[total // 2 - 1]
        middle2 = merged[total // 2]
        return (float(middle1) + float(middle2)) / 2.0

nums1 = list(map(int, input("Enter the first sorted array (space separated): ").replace(",", " ").split()))
nums2 = list(map(int, input("Enter the second sorted array (space separated): ").replace(",", " ").split()))

print("Output:", findMedianSortedArrays(nums1, nums2))

input("\nPress Enter to exit...")
