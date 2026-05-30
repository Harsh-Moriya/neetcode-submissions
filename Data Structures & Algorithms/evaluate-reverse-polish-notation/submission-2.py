class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for s in tokens:
            if not self.isOperator(s):
                nums.append(int(s))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                ans = self.operate(int(num1), int(num2), s)
                nums.append(ans)

        return nums[0]
    
    def isOperator(self, s: str) -> bool:
        return s == "+" or s == "-" or s == "*" or s == "/"

    def operate(self, num1: int, num2: int, o: str):
        match o:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)
            case _:
                return 0