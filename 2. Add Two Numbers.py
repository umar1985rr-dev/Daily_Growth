"""
LeetCode 2: Add Two Numbers

Aim:
Add two numbers represented as linked lists.

Explanation:
Each linked list stores digits in reverse order. Add them digit by digit while
maintaining the carry. Return the resulting linked list.

Algorithm:
1. Create a dummy node to store the result linked list.
2. Initialize a pointer (tail) to the dummy node and set carry = 0.
3. Traverse both linked lists simultaneously until both lists are exhausted and there is no carry left.
4. Read the current digit from each linked list. If a list has ended, consider its digit as 0.
5. Calculate the sum = digit1 + digit2 + carry.
6. Store the last digit of the sum (sum % 10) in a new node and attach it to the result linked list.
7. Update the carry = sum // 10.
8. Move to the next node in both linked lists (if available).
9. Repeat the process until all digits and the final carry are processed.
10. Return the linked list starting from the node next to the dummy node.

Sample Input:
First list: 2 4 3
Second list: 5 6 4

Expected Output:
Output: 7 -> 0 -> 8

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("Output:", " -> ".join(vals))

def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0
        total = digit1 + digit2 + carry
        digit = total % 10
        carry = total // 10
        tail.next = ListNode(digit)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next

arr1 = list(map(int, input("Enter first linked list digits (space separated): ").replace(","," ").split()))
arr2 = list(map(int, input("Enter second linked list digits (space separated): ").replace(","," ").split()))

l1 = build_list(arr1)
l2 = build_list(arr2)

result = addTwoNumbers(l1, l2)
print_list(result)

input("\nPress Enter to exit...")
