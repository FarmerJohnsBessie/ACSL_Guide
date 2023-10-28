from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BaseConversionForm, BaseCalculatorForm
import re


@csrf_exempt
def index(request):
    return render(request, 'base.html')


@csrf_exempt
def homepage(request):
    return render(request, 'pages/homepage.html')

@csrf_exempt
def base_converter(request):
    result_number = None

    if request.method == 'POST':
        form = BaseConversionForm(request.POST)
        if form.is_valid():
            source_base = form.cleaned_data['source_base']
            target_base = form.cleaned_data['target_base']
            input_number = form.cleaned_data['input_number']

            result_number = convert_base(source_base, target_base, input_number)
        form = BaseConversionForm()
    else:
        form = BaseConversionForm()

    return render(request, 'pages/base_converter.html', {'form': form, 'result_number': result_number})

@csrf_exempt
def base_calculator(request):
    result_number = None

    if request.method == 'POST':
        form = BaseCalculatorForm(request.POST)
        if form.is_valid():
            target_base = form.cleaned_data['target_base']
            input_expression = form.cleaned_data['input_expression']

            result_number = evaluate_expression(input_expression,target_base)
        form = BaseCalculatorForm()
    else:
        form = BaseCalculatorForm()

    return render(request, 'pages/base_calculator.html', {'form': form, 'result_number': result_number})

def convert_base(source_base, target_base, input_number):
    # Define a dictionary to map digits to their respective values
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert the input number to base 10
    decimal_number = 0
    input_number = str(input_number).upper()  # Convert to uppercase for A-Z digits
    for digit in input_number:
        decimal_number = decimal_number * source_base + digits.index(digit)

    # Convert the decimal number to the target base
    result_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        result_number = digits[remainder] + result_number
        decimal_number //= target_base

    return result_number

def base_to_decimal(num_str, base):
    '''Convert a number string from the specified base to base 10.'''
    return int(num_str.upper(), base)  # Use upper() to handle both uppercase and lowercase letters

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
    base10_expr = re.sub(r'[A-Za-z0-9]+(?:_\d+|\{(\d+)\})', convert_to_base10, expr)
    print(base10_expr)
    base10_value = eval(base10_expr)
    return convert_base(10,target_base,base10_value)
