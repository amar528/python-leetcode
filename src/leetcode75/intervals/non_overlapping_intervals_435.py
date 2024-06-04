from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        # sort by end time
        intervals.sort(key=lambda i: i[1])

        prev_end = 0
        for interval in intervals:
            if prev_end > interval[0]:
                count += 1
            prev_end = interval[1]

        return count
