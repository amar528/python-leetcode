class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        opening = ("(", "[", "{")
        mappings = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if mappings[popped] != c:
                        return False
                else:
                    return False

        if stack:
            return False

        return True
