import traceback
import sys

# inputs

# Sample Input 1

# inputs = {'H': 50, 'R': 10}
# code = """
# input H, R
# B = 0
# if H>48 then
#     B = B + (H - 48) * 2 * R: H = 48
# end if
# if H>40 then
#    B = B + (H - 40) * (3/2) * R
#    H = 40
# end if
# B = B + H * R
# output B
# """

# Sample Input 2

# inputs = {}
# code = '''
# A = “BANANAS”
# NUM = 0: T = “”
# for J = len(A) - 1 to 0 step -1
#      T = T + A[J]
# next
# for J = 0 to len(A) - 1
#     if A[J] == T(J) then NUM = NUM + 1
# next
# output NUM
# '''

# Sample Input 3

# inputs = {}
# code = """
# A(0) = 12: A(1) = 41: A(2) = 52
# A(3) = 57: A(4) = 77: A(5) = -100
# B(0) = 17: B(1) = 34: B(20) = 81
# J = 0: K = 0: N = 0
# while A(J) > 0
#   while B(K) <= A(J)
#     C(N) = B(K)
#     N = N + 1
#     K = K + 1
#   end while
#   C(N) = A(J): N = N + 1: J = J + 1
# end while
# C(N) = B(K)
# output C(4)
# """

# Sample Input 4

# input = {}
# code = """
# a = 1: b = 2: c = 3: d = 4: e = 4: f = 6
# if (d / b) < (f / a) then d = d / b
# a = f ↑ b / c ↑ (d / b)
# if (a <= f) && (b > e) then a = f else b = e
# if abs(c - f) != int(f / c) then c = f / c else f = f / c
# if (a = = b) || (c = = d) then a = a + b
# c = c + d
# output (b * c) * (f + d) / a / 2 * d - c + e ↑ (b - 2 * d)
# """

# Sample Input 5

# inputs = {'H': 50, 'R': 10}
# code = """input H, R
# B = 0
# if H>48 then
#     B = B + (H - 48) * 2 * R: H = 48
# end if
# if H>40 then
#    B = B + (H - 40) * (3/2) * R
#    H = 40
# end if
# B = B + H * R
# output B
# """

# Sample Input 6
#
# inputs = {}
# code = """
# a = '123'
# for i = 0 to len(a)
#     output a[i]
# next
# """

### NOTES ###

# STRING INDEXING NOT THE SAME AS PYTHON
# IF STATEMENT AND and OR DIFFERENT
# EXPONENT SIGN DIFFERENT
def solve(code, inputs):
    code = code.split('\n')
    pythoncode = ''' '''
    pythoncode += '\n'
    pythoncode += 'from math import sqrt, floor as flr \n'
    cur_indent = 0
    cur_input_index = 0
    input_list = inputs.split('\n')
    print(input_list)
    Py2PC = {}
    conditional_list = []
    cur_array_names = []


    # constant variables

    blank = ' '
    max_array_size = 10000
    function_list = ['abs', 'int', 'sqrt', 'len', 'range']
    INF = 999999999
    se_correspondence = {'if': 'end if', 'for': 'next', 'while': 'end while'}

    # Program

    def replace_paranthesis(string):
        if '(' in string and ')' in string and string[0] != '(':
            j = 0
            variable_name = ''
            while True:
                if string[j] == '(':
                    break
                variable_name += string[j]
                j += 1
            if variable_name not in function_list:
                new_string = string.replace('(', '[')
                new_string = new_string.replace(')', ']')
                return new_string
            else:
                return string
        else:
            return string

    def replace_exponents(string):
        new_string = ''
        for char in string:
            if char == '↑':
                new_string += '**'
            else:
                new_string += char
        return new_string

    def replace_int(string):
        new_string = list(string)
        for i in range(2, len(string)):
            if string[i] == 't' and string[i-1] == 'n' and string[i-2] == 'i':
                new_string[i] = 'r'
                new_string[i-1] = 'l'
                new_string[i-2] = 'f'
        return ''.join(list(map(str, new_string)))

    def replace_grammar(string):
        return replace_int(replace_exponents(replace_paranthesis(string)))



    for line in code:
        words = line.split()
        if not words:
            continue
        for word in words:
            if '(' in word and ')' in word and word[0] != '(':
                j = 0
                variable_name = ''
                while True:
                    if word[j] == '(':
                        break
                    variable_name += word[j]
                    j += 1
                if variable_name not in function_list and variable_name not in cur_array_names:
                    pythoncode += f'{variable_name} = [{INF} for _ in range({max_array_size})]\n'
                    cur_array_names.append(variable_name)

    cur_python_line = 2
    error = False
    output = False

    for u in range(1, len(code)+1):
        # print(pythoncode)
        line = code[u-1]
        words = line.split()
        if not words:
            continue
        try:
            if words[0] == 'input':
                for variable in words[1:]:
                    if variable[-1] == ',':
                        variable = variable[:-1]
                    pythoncode += f'{cur_indent * blank}{replace_grammar(variable)} = {replace_grammar(str(input_list[cur_input_index]))}\n'
                    cur_python_line += 1
                    cur_input_index += 1
                    Py2PC[cur_python_line] = u
                continue
            elif len(words) >= 2:
                if words[1] == '=':
                    i = 2
                    pythoncode += f'{cur_indent * blank}{replace_grammar(words[0])} = '
                    while i < len(words):
                        while "”" in words[i]:
                            words[i] = words[i].replace("”", "\"")
                        while "“" in words[i]:
                            words[i] = words[i].replace("“", "\"")
                        if words[i][-1] == ':':
                            var1 = replace_grammar(words[i][:-1])
                            var2 = replace_grammar(words[i + 1])
                            pythoncode += f'{var1}\n'
                            cur_python_line += 1
                            Py2PC[cur_python_line] = u
                            pythoncode += f'{cur_indent * blank}{var2} = '
                            i += 3
                            continue
                        var3 = replace_grammar(words[i])
                        pythoncode += var3
                        i += 1
                    pythoncode += '\n'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
                    continue
            if words[0] == 'if':
                conditional_list.append('if')
                if 'else' not in words:
                    pythoncode += f'{cur_indent * blank}if '
                    i = 1
                    while True:
                        if words[i] == 'then':
                            break
                        if words[i] == '&&':
                            pythoncode += ' and '
                        elif words[i] == '||':
                            pythoncode += ' or '
                        else:
                            pythoncode += replace_grammar(words[i])
                        i += 1
                    i += 1
                    if i != len(words):
                        pythoncode += f':\n{(cur_indent + 1) * blank}'
                        cur_python_line += 1
                        Py2PC[cur_python_line] = u
                        while i < len(words):
                            pythoncode += replace_grammar(words[i])
                            i += 1
                        pythoncode += '\n'
                        cur_python_line += 1
                        Py2PC[cur_python_line] = u
                    else:
                        pythoncode += ':\n'
                        cur_python_line += 1
                        Py2PC[cur_python_line] = u
                        cur_indent += 1
                else:
                    pythoncode += f'{cur_indent * blank}if '
                    i = 1
                    while True:
                        if words[i] == 'then':
                            break
                        if words[i] == '&&':
                            pythoncode += ' and '
                        elif words[i] == '||':
                            pythoncode += ' or '
                        else:
                            pythoncode += replace_grammar(words[i])
                        i += 1
                    i += 1
                    pythoncode += f':\n{(cur_indent + 1) * blank}'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
                    while True:
                        if words[i] == 'else':
                            break
                        pythoncode += replace_grammar(words[i])
                        i += 1
                    pythoncode += '\n'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
                    i += 1
                    pythoncode += f'{cur_indent*blank}else:\n'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
                    cur_indent += 1
                    pythoncode += cur_indent*blank
                    while i < len(words):
                        pythoncode += replace_grammar(words[i])
                        i += 1
                    cur_indent -= 1
                    pythoncode += '\n'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
            elif words[0] == 'end' and words[1] == 'if':
                last = conditional_list.pop()
                if last != 'if':
                    return (f"An error has occurred in line {u} of your pseudocode: invalid correspondence between 'end if' and if statement, do you mean '{se_correspondence[last]}'?")
                    error = True
                    break
                cur_indent -= 1
            elif words[0] == 'output':
                pythoncode += f"""{cur_indent * blank}if 'result' not in namespace: namespace['result'] = [\n"""
                for i in range(1, len(words)):
                    pythoncode += replace_grammar(words[i])
                pythoncode += ']\n'
                cur_python_line += 1
                Py2PC[cur_python_line] = u
                pythoncode += f"""{cur_indent * blank}else: namespace['result'].append(\n"""
                for i in range(1, len(words)):
                    pythoncode += replace_grammar(words[i])
                pythoncode += ')\n'
                cur_python_line += 1
                Py2PC[cur_python_line] = u
            elif words[0] == 'for':
                conditional_list.append('for')
                pythoncode += f"{cur_indent * blank}for {replace_grammar(words[1])} in range("
                cur_indent += 1
                i = 3
                while True:
                    if words[i] == 'to':
                        break
                    # return (words[i])
                    pythoncode += replace_grammar(words[i])
                    i += 1
                i += 1
                pythoncode += ','
                # print(i, words[i], words)
                while True:
                    if i == len(words):
                        break
                    if words[i] == 'step':
                        break
                    pythoncode += replace_grammar(words[i])
                    i += 1
                if i == len(words):
                    pythoncode += ",1):\n"
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
                else:
                    i += 1
                    pythoncode += ','
                    while i < len(words):
                        pythoncode += replace_grammar(words[i])
                        i += 1
                    pythoncode += '):\n'
                    cur_python_line += 1
                    Py2PC[cur_python_line] = u
            elif words[0] == 'next':
                if len(words) > 1:
                    return (f"An error has occurred in line {u} of your pseudocode: invalid syntax for 'next'")
                    error = True
                    break
                last = conditional_list.pop()
                if last != 'for':
                    return (f"An error has occurred in line {u} of your pseudocode: invalid correspondence between 'next' and for statement, do you mean '{se_correspondence[last]}'?")
                    error = True
                    break
                cur_indent -= 1
            elif words[0] == 'while':
                conditional_list.append('while')
                pythoncode += f'{cur_indent*blank}while '
                for i in range(1, len(words)):
                    pythoncode += replace_grammar(words[i])
                pythoncode += ':\n'
                cur_python_line += 1
                Py2PC[cur_python_line] = u
                cur_indent += 1
            elif words[0] == 'end' and words[1] == 'while':
                last = conditional_list.pop()
                if last != 'while':
                    return (f"An error has occurred in line {u} of your pseudocode: invalid correspondence between 'end while' and while statement, do you mean '{se_correspondence[last]}'?")
                    error = True
                    break
                cur_indent -= 1
            else:
                return (f"An error has occurred in line {u} of your pseudocode: invalid syntax")
                error = True
                break

            if words[0] == 'end' and len(words) == 1:
                return (f"An error has occured in line {u} of your pseudocode: invalid syntax for 'end'")
                error = True
                break

        except Exception as e:
            return (f"An error has occured in line {u} of your pseudocode: invalid syntax")
            error = True
            break

    # print(pythoncode)
    # print(Py2PC)
    # exec(pythoncode)

    if not error:
        try:
            namespace = {}
            exec(pythoncode, {'namespace': namespace})
            result = namespace.get('result', 'No result computed')
            str_result = ''
            for i in result:
                str_result += str(i)+"\n"
            return (str_result)
        except SyntaxError as e:
            # Return the line number from the SyntaxError exception
            return (f'An error has occurred in line {Py2PC[int(e.lineno)]} of your pseudocode: invalid syntax')
        except Exception as e:
            # For other exceptions, get the line number as before
            exc_type, exc_value, exc_traceback = sys.exc_info()
            line_number = traceback.extract_tb(exc_traceback)[-1].lineno
            return (f'An error has occurred in line {Py2PC[int(line_number)]} of your pseudocode: {e}')

# print(solve(code, inputs))