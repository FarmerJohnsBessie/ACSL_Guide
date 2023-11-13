from sympy import symbols, sympify

x = symbols('x')

def f(x_val, recursion_statement, recursion_conditional):
    # Use the sympify function to handle symbolic variables in the condition
    for statement, condition in zip(recursion_statement, recursion_conditional):
        # Check the condition for x
        if sympify(condition).subs(x, x_val):
            if 'f(' in statement:
                # Extract the recursive part, assuming the format is 'f(expression)'
                start = statement.find('f(') + 2
                end = statement.rfind(')')
                recursive_part = statement[start:end]

                # Recursively call f with the new x value from recursive_part
                new_x_val = sympify(recursive_part).subs(x, x_val)
                return f(new_x_val, recursion_statement, recursion_conditional) + sympify(statement[end + 1:]).subs(x, x_val)
            else:
                # Base case, directly return the evaluated statement
                return sympify(statement).subs(x, x_val)

    # If no condition is met (which shouldn't happen), return None
    return 'Error'

x, y = symbols('x y')

def evaluate_condition(condition, variables):
    condition = condition.replace('&', ' and ').replace('|', ' or ')
    return sympify(condition).subs(variables)

def parse_recursive_statement(statement, variables):
    if 'f(' in statement:
        start = statement.find('f(') + 2
        end = statement.rfind(')')
        recursive_part = statement[start:end].split(',')
        new_values = [sympify(expr).subs(variables) for expr in recursive_part]
        remaining_statement = statement[end+1:]
        return new_values, remaining_statement
    else:
        return None, statement

def recursive_function(variables, recursion_statement, recursion_conditional):
    for statement, condition in zip(recursion_statement, recursion_conditional):
        if evaluate_condition(condition, variables):
            new_values, remaining_statement = parse_recursive_statement(statement, variables)
            if new_values:
                new_variables = dict(zip(['x', 'y'], new_values))
                # Call recursive function with new variables
                val = recursive_function(new_variables, recursion_statement, recursion_conditional)
                if val is not None:  # Check if value is not None
                    return val + sympify(remaining_statement).subs(variables)
            else:
                return sympify(statement).subs(variables)
    return None
