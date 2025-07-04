class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # division truncate toward zero
                    # корректное усечение для отрицательных чисел:
                    stack.append(int(a / b) if a * b >= 0 else -(-a // b))
            else:
                stack.append(int(token))
        return stack.pop()
