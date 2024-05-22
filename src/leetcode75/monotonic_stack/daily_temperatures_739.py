from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n

        # monotonic non-increasing stack
        monotone_stack = []

        for i in range(n):

            # pop from the stack whilst it has elements
            # and the top of the stack is less than the current value
            # the stack values are the corresponding array index
            while monotone_stack and temperatures[monotone_stack[-1]] < temperatures[i]:
                # the answer for the ith temperate will be the first index on the stack that is
                # greater - so current i - index is the number of days until the value is greater
                result[monotone_stack[-1]] = i - monotone_stack[-1]
                monotone_stack.pop()

            # push this index onto the stack
            monotone_stack.append(i)

        return result
