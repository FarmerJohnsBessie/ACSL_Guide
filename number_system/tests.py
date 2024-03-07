from django.test import TestCase


# Create your tests here.
instruction = """
Your task is to generate and solve random ACSL (American Computer Science League) questions similar to the ones on the real contest.
The questions should be diverse, unique, and varying in difficulty based on the user input. 
Even though the questions should be unique, you should still stick to the general format of ACSL questions.
After you finish generating the questions, you should provide an accurate solution to the question you randomly generated.
Your solution do not have to include step-by-step process, only include the actual answer itself.
When calculating the answers, make sure to abide by specific ACSL rules and notations even if it is different from standard conventions.
"""

input_format = """
All questions asked to you will be in the format of "[(topic)] [(desired difficulty)] [(other notes)]"
There are 3 possible inputs for topic:
    1. Bit-string Flicking
    2. Prefix/Infix/Postfix Notation
    3. LISP
The desired difficulty will be a number from 1-5, with 1 being the least difficult and 5 being the most difficult.
The other notes is an optional input parameter, and could be empty.
"""


output_format = """
Output using JSON format.
1. The first key of the JSON dictionary should be a string called "question", in which the value should be the random question you generated in string data type.
2. The second key of the JSON dictionary should be a string called "answer", in which the value should be the answer of the random question you generated in string data type. 
"""

# 多轮对话的例子
examples = """
[Bit-string Flicking] [1] []

{"question": "1001 AND 1100, "answer": "1000"}

[Bit-string Flicking] [2] []

{"question": "1001 AND 1000 OR 0001", "answer": "1001"}

[Bit-string Flicking] [3] []

{"question": "(101110 AND NOT 110110 OR (LSHIFT-3 101010))", "answer": "011000"}

[Bit-string Flicking] [3] [Generate a question that only contains LCIRC and RCIRC for notations]

{"question": "(RSHIFT-1 (LCIRC-4 (RCIRC-2 01101)))", "answer": "01010"}

[Bit-string Flicking] [4] [question where the numbers for LCIRC and RCIRC are big]

{"question": "((RCIRC-14 (LCIRC-23 01101)) | (LSHIFT-1 10011) & (RSHIFT-2 10111))", "answer": "10110"}

[Bit-string Flicking] [5] []

{"question": "List all possible values of x (5 bits long) that solve the following equation: (LSHIFT-1 (10110 XOR (RCIRC-3 x) AND 11011)) = 01100", "answer": "00000, 00001, 00100, 00101"}
"""

user_input = "[Bit-string Flicking] [2]"

prompt = f"""
{instruction}

{input_format}

{output_format}

Examples:
{examples}

User Input: {user_input}
"""

print(prompt)