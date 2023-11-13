import os
from openai import OpenAI

client = OpenAI()

# ======================Files======================
recursion_file = client.files.create(
    file=open("pdfs/Recursive Functions.pdf", "rb"),
    purpose='assistants'
)

pseudo_code_file = client.files.create(
    file=open("pdfs/What does this program do.pdf", "rb"),
    purpose='assistants'
)

assistant = client.beta.assistants.create(
    name="ACSL Assistant",
    instructions='''You are a robot that can answer every questions from the ACSL competition. ACSL Competition is a 
    computer science competition. Therefore, you can only answer questions related to computer science. You can 
    answer questions related to the following topics: 
    1. Computer Number Systems (Question related to Binary, Octal, Decimal, Hexadecimal) 
    2. Recursion (Question related to recursive functions) 
    3. Psuedocode (Questions that ask what does this psuedocode do) 
    If you are not sure about the answer or not sure what to do, just output "I don't know" instead of trying to answer the question. 
    If a user asks a question that's not related to computer science, you MUST tell them that this is not related to ACSL and you can not answer this question.
    You have access to some files that contains instructions and examples to various ACSL topics. 
    These files can help you answer the questions. For example, the file "Recursive Functions.pdf" contains instructions and examples to recursive functions,
    and the file "What does this program do.pdf" contains the grammar and examples to psuedocode.
    ''',
    tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
    model="gpt-4-1106-preview",
    file_ids=[recursion_file.id, pseudo_code_file.id]
)

thread = client.beta.threads.create()

recursion_statement = ['3*x+2', 'f(x-1)+4']
recursion_conditional = ['x<3', 'x>=3']

recursion_solving_prompt = '''
Please solve the recursion question below. 

Instructions:
 - I am going to define a recursive function below. And your job is to evaluate the function at a given input.
 - If you are unsure about an answer, then output an error. Accuracy is the most important thing.
 - Don't try to answer if you don't know. You must ensure a correct answer.
 - Think step by step. List every steps out in the STEPS section in the output. Include as many detail as you can.


Note:
 - The function may be in the form of f(x) or f(x,y).
 - You will see which form the function is in using the question.

Error Output Format:
 - If there are mistakes in the questions, output in this format: 
 - ERROR: (error here)

Common errors:
1. Inconsistent Parameters. (Ex: both f(x-1) and f(x-1,y-2) appears in the same recursive function)
2. Infinite loop (stack overflow/ can't evaluate the function)
3. Wrong function (the function should be f(x)/f(x,y), any other functions such as g(x) in the question should be wrong)
4. Undefined Variable (any variable that are not defined are wrong. such as a,b,c. Note that y shouldn't appear in f(x))
5. Anything that's not a math expression. (such as english words and weird symbols)
6. Anything that you think it's a mistake. (Anyting that blocks you from solving the question)

Output Format:
 - Don't say anything that's unnecessary to answering the question, and format your output in this way:

 STEPS:
 (The steps you used to solve this question. Do it step by step to increase your accuarcy)

 ANSWER:
 (Your final answer to the question here)


Define f(x)/f(x,y) = 

'''
for i in range(len(recursion_statement)):
    line = f"{recursion_statement[i]} if {recursion_conditional[i]}"
    recursion_solving_prompt += line + "\n"

recursion_solving_prompt += '''
Problem Statement:
Evaluate f(5).
'''

pseudo_code_solving_prompt = '''
Please solve the pseudo code question below.

Instructions:
 - You will be given a pseudo code and a problem statement (Ex. what the program will output)
 - Your job is to follow the instruction given and output the correct answer. 
 - Think step by step and keep trak of all the variables. 
 - List every steps out in the STEPS section in the output. Include as many detail as you can.
 - You must ensure the accuracy of the answer. If you are not sure about the answer, then output an error!

Note: 
 - This pseudo code is different from normal pseudo code. 
 - This is a pseudo code that is designed for the ACSL competition. 
 - For all the grammar rules, refer to the ACSL documents passed in.
 - For examples, also refer to the ACSL documents passed in.

Handle Errors:
 - If there are errors in the code, then don't output any answers, just output:
 - ERROR: (error here)

Common Errors:
1. Anything that doesn't follow the grammar.
2. Any compile errors. (variable not defined, index out of range etc.)
3. Basically any regular errors that a IDE will tell you.
4. If the code is too long or you can not handel it, then output an error.
5. If you are not sure about the answer, then output an error. 
6. Anything that you think it's a mistake. (Anyting that blocks you from solving the question)

Output Format:
 - Don't say anything that's unnecessary to answering the question, and format your output in this way:

 STEPS:
 (The steps you used to solve this question. Do it step by step to increase your accuarcy)

 ANSWER:
 (Your final answer to the question here)


Pseudo Code:

'''

pseudo_code_solving_prompt += '''
Problem Statement:

'''

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=recursion_solving_prompt
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions=""
)
while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    if run.status == "completed":
        break
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
first_message_value = messages.data[0].content[0].text.value
print(first_message_value)