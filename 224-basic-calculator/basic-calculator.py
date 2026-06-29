class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1  # 1 for '+', -1 for '-'

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1
            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1
            elif ch == '(':
                # save current result and sign, start fresh for the sub-expression
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()   # sign that applied to this parenthesis
                result += stack.pop()   # result accumulated before the parenthesis
            # spaces are ignored

        result += sign * number
        return result