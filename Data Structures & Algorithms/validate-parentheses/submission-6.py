class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for c in s:
            if c in brackets:
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0