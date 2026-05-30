class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            a = b = 0

            if s in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

            match s:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(int(a / b))
                case _:
                    stack.append(int(s))

        return stack[0]