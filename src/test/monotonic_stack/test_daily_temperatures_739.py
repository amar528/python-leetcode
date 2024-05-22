from unittest import TestCase

from leetcode75.monotonic_stack.daily_temperatures_739 import Solution


class TestSolution(TestCase):
    def test_daily_temperatures_example1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

        sol = Solution()
        result = sol.dailyTemperatures(temperatures)

        self.assertListEqual([1, 1, 4, 2, 1, 1, 0, 0], result)

    def test_daily_temperatures_example2(self):
        temperatures = [30, 40, 50, 60]

        sol = Solution()
        result = sol.dailyTemperatures(temperatures)

        self.assertListEqual([1, 1, 1, 0], result)

    def test_daily_temperatures_example3(self):
        temperatures = [30, 60, 90]

        sol = Solution()
        result = sol.dailyTemperatures(temperatures)

        self.assertListEqual([1, 1, 0], result)

    def test_daily_temperatures_example4(self):
        temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]

        sol = Solution()
        result = sol.dailyTemperatures(temperatures)

        self.assertListEqual([8, 1, 5, 4, 3, 2, 1, 1, 0, 0], result)
