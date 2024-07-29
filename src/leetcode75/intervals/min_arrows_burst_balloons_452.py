from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # intervals - sort by start time
        points.sort()

        prev = points[0]
        n = len(points)
        arrows = n

        for i in range(1, n):

            curr = points[i]

            # overlap ?
            if curr[0] <= prev[1]:
                # yes, overlap, one less arrow needed
                arrows -= 1

                # update previous interval
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                # no overlap, just update previous
                prev = curr

        return arrows
    