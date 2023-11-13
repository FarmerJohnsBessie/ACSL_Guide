import re
from random import randint


def convert_base(source_base, target_base, input_number):
    # Define a dictionary to map digits to their respective values
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Check for invalid source and target bases
    if source_base < 2 or source_base > len(digits) or target_base < 2 or target_base > len(digits):
        raise ValueError("Invalid source or target base")

    # Convert the input number to base 10
    decimal_number = 0
    input_number = str(input_number).upper()  # Convert to uppercase for A-Z digits
    for digit in input_number:
        digit_value = digits.find(digit)
        if digit_value == -1 or digit_value >= source_base:
            raise ValueError(f"Invalid digit '{digit}' for source base {source_base}")
        decimal_number = decimal_number * source_base + digit_value

    # Convert the decimal number to the target base
    result_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        result_number = digits[remainder] + result_number
        decimal_number //= target_base

    return result_number

def base_to_decimal(num_str, base):
    '''Convert a number string from the specified base to base 10.'''
    try:
        return int(num_str.upper(), base)  # Use upper() to handle both uppercase and lowercase letters
    except ValueError:
        raise ValueError(f'Invalid digit for base {base}. Base must be >= 2 and <= 36')

def convert_to_base10(match):
    '''Convert matched string to base 10.'''
    # If the string contains '_', it has a base
    if '_' in match.group():
        num_str, base_str = match.group().split('_')
        base = int(re.search(r'\d+', base_str).group())
        value = base_to_decimal(num_str, base)
    # Else, it's already in base 10
    else:
        value = int(match.group())
    return str(value)

def evaluate_expression(expr, target_base):
    '''Evaluate a mixed-base expression, converting it to base 10 first.'''
    # Convert all numbers to base 10
    # The pattern now matches alphanumeric strings followed by optional '_base'
    base10_expr = re.sub(r'[A-Za-z0-9]+_\{?\d+\}?', convert_to_base10, expr)
    print(base10_expr)
    base10_value = eval(base10_expr)
    return convert_base(10,target_base,base10_value)

def generate_question(difficulty="Junior"):
    type_of_question = randint(1, 2)
    if type_of_question <= 2:
        if difficulty == 'Intermediate' or difficulty == 'Senior':
            base1 = randint(2, 12)
            if base1 > 10:
                base1 = randint(1, 2)
                if base1 == 1:
                    base1 = randint(11, 15)
                else:
                    base1 = 16
                    base1 = randint(2, 12)

            while True:
                base2 = randint(2, 12)
                if base2 > 10:
                    base2 = randint(1, 2)
                    if base2 == 1:
                        base2 = randint(11, 15)
                    else:
                        base2 = 16
                if base2 != base1:
                    break
        else:
            base1 = randint(1, 4)
            while True:
                base2 = randint(1, 4)
                if base1 != base2:
                    break

            dbase = {1: 2, 2: 8, 3: 10, 4: 16}
            base1 = dbase[base1]
            base2 = dbase[base2]

        if difficulty == 'Junior':
            maximum = randint(4, 5)
        elif difficulty == 'Intermediate':
            maximum = randint(6, 7)
        elif difficulty == 'Senior':
            maximum = randint(8, 9)
        else:
            maximum = 8

        number_of_digits = randint(2, maximum)
        number = ''
        d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        for _ in range(number_of_digits):
            n = randint(0, base1 - 1)
            if n < 10:
                number += str(n)
            else:
                number += d[n]
    while True:
        if number[0] == '0':
            number = number[1:]
        else:
            break

    question_text = f'Please convert the follow number {number} from base-{base1} to base-{base2}'
    print(question_text)

    def convert_base(num_str, from_base=10, to_base=10):
        """Convert a number from one base to another."""

        # Convert the number from the given base to base 10
        def to_base_10(num_str, base):
            num_str = num_str[::-1]  # reverse the string for easier processing
            num = 0
            for i, digit in enumerate(num_str):
                if '0' <= digit <= '9':
                    val = int(digit)
                else:
                    val = 10 + ord(digit.upper()) - ord('A')
                num += val * (int(base) ** int(i))
            return num

        # Convert a number from base 10 to the desired base
        def from_base_10(num, base):
            digits = []
            while num:
                val = num % base
                if 0 <= val <= 9:
                    digits.append(str(val))
                else:
                    digits.append(chr(ord('A') + val - 10))
                num //= base
            return ''.join(reversed(digits)) or '0'

        num_in_base_10 = to_base_10(num_str, from_base)
        return from_base_10(num_in_base_10, to_base)

    correct_answer = str(convert_base(num_str=number, from_base=base1, to_base=base2))
    return {"question":question_text, "answer":correct_answer}

