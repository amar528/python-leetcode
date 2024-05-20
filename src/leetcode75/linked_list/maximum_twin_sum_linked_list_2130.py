import sys
from typing import Optional

from leetcode75.linked_list.listnode import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # find middle of list using fast/slow pointer
        # push values to a stack as we go
        stack = []
        slow = head
        fast = head

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # slow is now at middle
        # iterate from there, compare with popped values from the stack
        curr = slow
        max_pair_sum = -sys.maxsize
        while curr:
            popped_val = stack.pop()
            max_pair_sum = max(max_pair_sum, popped_val + curr.val)
            curr = curr.next

        return max_pair_sum
