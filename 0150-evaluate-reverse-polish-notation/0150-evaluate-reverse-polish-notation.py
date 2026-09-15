class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = { "+" : 1, "-": 2, "*": 3, "/": 4}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num1+num2)
                elif tokens[i] == "-":
                    stack.append(num1-num2)
                elif tokens[i] == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
        return stack[-1]

        