def twoSum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

nums = list(map(int, input("Enter the array elements separated by space: ").replace(","," ").split()))
target = int(input("Enter the target value: "))

result = twoSum(nums, target)
print("Output:", result)

input("\nPress Enter to exit...")
