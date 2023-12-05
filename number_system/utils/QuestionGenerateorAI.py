from openai import OpenAI

client = OpenAI()

thread = client.beta.threads.create()


def generate_question(question_type, difficulty):
    files = {
        'Computer_Number_Systems': 'file-CQ7N9RnwoPQMYup3kZSYgtQF',
        'Recursive_Functions': 'file-9rA4i6x6ZOTP0ffbDvVo9foO',
        'What_Does_This_Program_Do': 'file-N65Qf7gOUYBuUAjyDH51NsnC'
    }
    language = {
        'Computer_Number_Systems': 'computer number systems',
        'Recursive_Functions': 'revcursive functions',
        'What_Does_This_Program_Do': 'ACSL pseudocode'
    }

    sample_outputs = {
        'Recursive_Functions': r'''
Problem:
Consider the recursive function \( W(x) \) defined by the following rules:

\[ W(x) = \begin{cases} 
3x + 1 & \text{if } x \leq 5 \\
W(x - 2) - 1 & \text{if } x > 5 
\end{cases} \]

Calculate the value of \( W(9) \).

Steps:
\[ W(9) = W(7) - 1 \]
\[ W(7) = W(5) - 1 \]
\[ W(5) = 3 \times 5 + 1 = 16 \]
Substitute \( W(5) \) back into the previous expression:
\[ W(7) = 16 - 1 = 15 \]
Substitute \( W(7) \) back into the initial expression:
\[ W(9) = 15 - 1 = 14 \]
Therefore, the value of \( W(9) \) is \( 14 \).

Answer:
14
        ''',
        'Computer_Number_Systems': r'''
Problem:
Solve for x where \(x_{16}\)=\(3676_{8}\)

Steps:
One method of solution is to convert \(3676_{8}\) into base 10, and then convert that number into base 16 to yield the value of x.

An easier solution, less prone to arithmetic mistakes, is to convert from octal (base 8) to hexadecimal (base 16) through the binary (base 2) representation of the number:

\[ 3676_{8} = 011 110 111 110_{2} \]
\[ 011 110 111 110_{2} = 7BE_{16} \]
Answer:
\(7BE_{16}\)
        ''',
        'What_Does_This_Program_Do': 'sort'
    }
    prompt = f'''
    read the PDF file {files[question_type]} and create a unique {difficulty} {language[question_type]} question that has the same style. 
    Same style also means the the format of math expressions.
    Based on the style and format of the provided examples and sample problems from the PDF file, {difficulty} {language[question_type]} question.

    Also output the steps you took to solve the question. (basically the math you did).
    
    This is a sample output for a {language[question_type]} question:
    {sample_outputs[question_type]}


    output math in mathjax formula.
    follow the output format strictly, do not change the format, do not output any other things.
    you need to output both the problem, steps and answer in the correct format in your last response.
    DO NOT OUTPUT ANYTHING THAT DOESN't FOLLOW THE OUTPUT FORMAT!!!
    '''

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_7FtHyXIwL5vSlsDgBHBaMyPn",
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
    return first_message_value

