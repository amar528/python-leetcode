class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if text1 == text2:
            return len(text1)

        # tabular representation of common lengths We calculate the values in a bottum-up manner text1 = rows (
        # vertical axis) text2 = cols (horizontal axis) If we have a match at i,j then we +1 to the diagonal value at
        # [i + 1][j + 1] If there is no match, then we set the value at i,j tp the max() of the values: to the right
        # (j + 1) and down (i + 1)
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):  # rows
            for j in reversed(range(len(text2))):  # col

                if text1[i] == text2[j]:
                    # diagonally - accumulate from i+1, j+1
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # We set i,j to the max of the cells to the right, and down
                    dp[i][j] += max(dp[i + 1][j], dp[i][j + 1])

        # the answer will have accumulated up to the initial cell
        return dp[0][0]
