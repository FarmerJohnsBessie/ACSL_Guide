from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BaseConversionForm


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
    else:
        form = BaseConversionForm()

    return render(request, 'pages/base_converter.html', {'form': form, 'result_number': result_number})

def convert_base(source_base, target_base, input_number):
    # Define a dictionary to map digits to their respective values
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert the input number to base 10
    decimal_number = 0
    input_number = input_number.upper()  # Convert to uppercase for A-Z digits
    for digit in input_number:
        decimal_number = decimal_number * source_base + digits.index(digit)

    # Convert the decimal number to the target base
    result_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        result_number = digits[remainder] + result_number
        decimal_number //= target_base

    return result_number