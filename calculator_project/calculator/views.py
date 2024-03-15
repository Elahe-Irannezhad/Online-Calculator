from django.http import HttpResponse
from django.views.decorators.http import require_GET

def calculate(request):

    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))
    op = request.GET.get('op')

    if op == "add":
        result = n1 + n2
        operator = "+"

    elif op == "subtract":
        result = n1 - n2
        operator = "-"

    elif op == "multiply":
        result = n1 * n2
        operator = "*"

    elif op == "divide":
        if n2 == 0:
            return HttpResponse("Division by Zero Is Not Allowed.")
        result = n1 / n2
        operator = "/"

    else:
        return HttpResponse("Invalid Operator.")

    return HttpResponse(f"Result of {n1} {operator} {n2} is {result}.")