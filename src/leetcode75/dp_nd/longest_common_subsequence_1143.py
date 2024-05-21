class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # tabular representation of common lengths
        # text1 = rows (vertical axis)
        # text2 = cols (horizontal axis)
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):  # rows
            for j in range(len(text2)):  # cols
                if text1[i] == text2[j]:
                    dp[i][j] += 1

        return 0
