import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..forms import BaseConversionForm, BaseCalculatorForm
from django.contrib import messages
from django.shortcuts import render
from number_system.utils import NumberSystem, PCSolver
from ..utils.RecursiveFunction import solve2, solve1
from ..utils.PrefixInfixPostfix import output
from ..utils.BitStringFlicking import evaluate_expression

def tools(request):
    return render(request, 'pages/tool_box.html')


@csrf_exempt
def base_converter(request):
    if request.method == 'POST':
        form = BaseConversionForm(request.POST)
        if form.is_valid():
            source_base = form.cleaned_data['source_base']
            target_base = form.cleaned_data['target_base']
            input_number = form.cleaned_data['input_number']

            try:
                result_number = NumberSystem.convert_base(source_base, target_base, input_number)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Invalid input. Please check your values.")
    else:
        form = BaseConversionForm()

    return render(request, 'pages/contest1/base_converter.html', {'form': form})


@csrf_exempt
def base_calculator(request):
    result_number = None

    if request.method == 'POST':
        form = BaseCalculatorForm(request.POST)
        if form.is_valid():
            target_base = form.cleaned_data['target_base']
            input_expression = form.cleaned_data['input_expression']
            try:
                result_number = NumberSystem.evaluate_expression(input_expression, target_base)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = BaseCalculatorForm()

    return render(request, 'pages/contest1/base_calculator.html', {'form': form, 'result_number': result_number})


@csrf_exempt
def recursion_solver(request):
    return render(request, 'pages/contest1/recursive_solver.html')


def solve_recursion(request):
    data = json.loads(request.body)
    equations = data['equations']
    conditions = data['conditions']
    value = data['value']
    # if len(value) == 1:
    #     value = value[0]
    # else:
    #     value = value[0] + ',' + value[1]
    # str = RecursiveFunctionAI.recursive_function_solver(equations, conditions, value)
    # return JsonResponse({'result': str})
    if len(value) == 1:
        result = solve1(equations, conditions, int(value[0]))
    else:
        result = solve2(equations, conditions, int(value[0]), int(value[1]))

    if result == "Error":
        return JsonResponse({'result': 'Error'})
    else:
        return JsonResponse({'result': str(result)})


@csrf_exempt
def ide(request):
    return render(request, 'pages/contest1/IDE.html')


def ide_run(request):
    data = json.loads(request.body)
    code = data['code']
    language = data['language']
    inputs = data['inputs']
    if language == 'pseudo':
        result = PCSolver.solve(code, inputs)
    elif language == 'LISP':
        result = "We are still working on this"
    elif language == 'assembly':
        result = "We are still working on this"
    else:
        result = "Internal Server Error"

    return JsonResponse({'output': result})


def prefix_infix_postfix(request):
    return render(request, 'pages/contest2/prefix_infix_postfix.html')


def prefix_infix_postfix_solver(request):
    data = json.loads(request.body)
    expression = data['expression']
    inputType = data['inputType']
    outputType = data['outputType']

    if inputType == "prefix":
        inputType = 1
    elif inputType == 'infix':
        inputType = 2
    elif inputType == 'postfix':
        inputType = 3
    else:
        inputType = 4

    if outputType == "prefix":
        outputType = 1
    elif outputType == 'infix':
        outputType = 2
    elif outputType == 'postfix':
        outputType = 3
    else:
        outputType = 4

    try:
        result = output(expression,inputType, outputType)
    except Exception:
        result = "There is an error."
    return JsonResponse({'output': result})


def bit_string_flicking(request):
    return render(request, 'pages/contest2/Bit_String_Flicking.html')


def bit_string_flicking_solver(request):
    data = json.loads(request.body)
    expression = data['expression']
    output = evaluate_expression(expression)
    return JsonResponse({'output':output})

def bit_string_flicking_equation_solver(request):
    data = json.loads(request.body)
    equation = data['equation']
    bit_string_length = data['bit_string_length']
    return JsonResponse({'output':'hi'})