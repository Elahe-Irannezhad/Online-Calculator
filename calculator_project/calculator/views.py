from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from .models import UserAction

@login_required
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
    
    actionRecord = f"User Performed {op}."
    userAction = UserAction.objects.create(user = request.user, action = actionRecord)

    return HttpResponse(f'{n1} {operator} {n2} = {result}')
