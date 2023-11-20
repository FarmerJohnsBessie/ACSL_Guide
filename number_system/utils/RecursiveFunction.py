from sys import setrecursionlimit
setrecursionlimit(10**3)

def f(x, statements, conditionals):
    for i, condition in enumerate(conditionals):
        if eval(condition):
            statement = statements[i].replace('f()', 'f(x, statements, conditionals)')
            return eval(statement)
    return "No condition met"

def f2(x, y, statements, conditionals):
    for i, condition in enumerate(conditionals):
        if eval(condition):
            statement = statements[i].replace('f2()', 'f2(x, y, statements, conditionals)')
            return eval(statement)
    return "No condition met"

def convert(recursion_statements, is_two_variable):
    recursion_statements_code = []
    for a in recursion_statements:
        open_bracket_cnt = 0
        cur = ''
        for i in range(len(a)):
            if a[i] == '(':
                open_bracket_cnt += 1
            if a[i] == ')':
                open_bracket_cnt -= 1
            if open_bracket_cnt == 1 and a[i + 1] == ')':
                cur += a[i]
                cur += ',statements,conditionals'
            elif a[i] == 'f' and is_two_variable:
                cur += a[i]
                cur += '2'
            else:
                cur += a[i]
        recursion_statements_code.append(cur)
    return recursion_statements_code

def convert_conditional(conditional):
    recursion_conditional = []
    bad_list = ['<', '>', '=']
    for a in conditional:
        cur = ''
        for i in range(len(a)):
            if a[i] == '=' and a[i+1] != '=' and a[i-1] not in bad_list:
                cur += '=='
            else:
                cur += a[i]
        recursion_conditional.append(cur)
    return recursion_conditional

def solve1(statement, conditional, x):
    recursion_statement_code = convert(statement, is_two_variable=False)
    conditional = convert_conditional(conditional)
    result = f(x, recursion_statement_code, conditional)
    return result

def solve2(statement, conditional, x, y):
    recursion_statements_code = convert(statement, is_two_variable=True)
    conditional = convert_conditional(conditional)
    result = f2(x, y, recursion_statements_code, conditional)
    return result

# inputs
# recursion_statements = ['f(x-7)+1', 'x', 'f(x+3)']
# recursion_conditionals = ['x>5', '0<=x<=5', 'x<0']

# recursion_statements = ['f(x-y, y-1)+2', 'x+y']
# recursion_conditionals = ['x>y', 'x<=y']

# recursion_statements = ['f(x-1, y+2)+3', '2*f(x+1, y-1)-5', 'x*x+y']
# recursion_conditionals = ['x>y', 'x<y', 'x=y']

