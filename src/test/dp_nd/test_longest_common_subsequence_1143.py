from unittest import TestCase

from leetcode75.dp_nd.longest_common_subsequence_1143 import Solution


class TestSolution(TestCase):
    def test_longest_common_subsequence_example1(self):
        text1 = "abcde"
        text2 = "ace"

        sol = Solution()
        result = sol.longestCommonSubsequence(text1, text2)

        # 'ace'
        self.assertEqual(3, result)

    def test_longest_common_subsequence_example2(self):
        text1 = "abc"
        text2 = "abc"

        sol = Solution()
        result = sol.longestCommonSubsequence(text1, text2)

        # 'abc'
        self.assertEqual(3, result)

    def test_longest_common_subsequence_example3(self):
        text1 = "abc"
        text2 = "def"

        sol = Solution()
        result = sol.longestCommonSubsequence(text1, text2)

        self.assertEqual(0, result)

    def test_longest_common_subsequence_example14(self):
        text1 = "ezupkr"
        text2 = "ubmrapg"

        sol = Solution()
        result = sol.longestCommonSubsequence(text1, text2)

        self.assertEqual(2, result)
