import sys
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        # sort by end time
        intervals.sort(key=lambda i: i[1])

        # keep track of the previous end time
        prev_end = -sys.maxsize
        for interval in intervals:

            # does the previous end time overlap with the new start time
            if prev_end > interval[0]:
                count += 1
            else:
                prev_end = interval[1]

        return count
