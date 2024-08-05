import math


class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        curr_num = 0
        previous_op = "+"

        for c in s + "+":

            if c.isdigit():
                curr_num = (curr_num * 10) + (int(c))

            elif c in "+-/*":

                if previous_op == "+":
                    stack.append(curr_num)
                elif previous_op == "-":
                    stack.append(-curr_num)
                elif previous_op == "*":
                    stack.append(stack.pop() * curr_num)
                elif previous_op == "/":
                    stack.append(math.trunc(stack.pop() / curr_num))

                previous_op = c
                curr_num = 0

        # Now process the stack, adding all the numbers
        return sum(stack)
