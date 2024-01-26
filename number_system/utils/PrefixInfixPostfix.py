class ExpressionConverter:
    def __init__(self):
        self.precedence = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operand(self, c):
        return c.isalpha() or c.isdigit()

    def is_operator(self, c):
        return c in self.precedence

    def infix_to_postfix(self, infix):
        result = []
        stack = []
        infix = infix.split()
        for token in infix:
            if self.is_operand(token):
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence[token] <= self.precedence[stack[-1]]:
                    result.append(stack.pop())
                stack.append(token)
        while stack:
            result.append(stack.pop())
        return ' '.join(result)

    def infix_to_prefix(self, infix):
        infix = infix.split()
        infix = list(reversed(['(' if token == ')' else ')' if token == '(' else token for token in infix]))
        postfix = self.infix_to_postfix(infix)
        prefix = list(reversed(postfix.split()))
        return ' '.join(prefix)

    def prefix_to_infix(self, prefix):
        stack = []
        for token in reversed(prefix.split()):
            if self.is_operand(token):
                stack.append(token)
            elif self.is_operator(token):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(f"({op1} {token} {op2})")
        return stack[-1]

    def postfix_to_infix(self, postfix):
        stack = []
        for token in postfix.split():
            if self.is_operand(token):
                stack.append(token)
            elif self.is_operator(token):
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(f"({op1} {token} {op2})")
        return stack[-1]

    def postfix_to_prefix(self, postfix):
        stack = []
        for token in postfix.split():
            if self.is_operand(token):
                stack.append(token)
            elif self.is_operator(token):
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(f"{token} {op1} {op2}")
        return ' '.join(stack)

    def prefix_to_postfix(self, prefix):
        stack = []
        for token in reversed(prefix.split()):
            if self.is_operand(token):
                stack.append(token)
            elif self.is_operator(token):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(f"{op1} {op2} {token}")
        return ' '.join(stack)

converter = ExpressionConverter()

# Sample Input 1
expr = "3 4 * 8 2 / + 7 5 - ^"
start = 3
end = 1

def output(expr, start, end):
    if start == 1:
        if end == 1:
            return expr
        elif end == 2:
            return converter.prefix_to_infix(expr)
        elif end == 3:
            return converter.prefix_to_postfix(expr)
    elif start == 2:
        if end == 1:
            return converter.infix_to_prefix(expr)
        elif end == 2:
            return expr
        elif end == 3:
            return converter.infix_to_postfix(expr)
    elif start == 3:
        if end == 1:
            return converter.postfix_to_prefix(expr)
        elif end == 2:
            return converter.postfix_to_infix(expr)
        elif end == 3:
            return expr

print(output(expr, start, end))