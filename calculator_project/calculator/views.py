from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from .models import UserAction
from django.shortcuts import render

@login_required
def calculate(request):

    if request.method == 'POST':
        
        n1 = int(request.POST.get('n1', ''))
        n2 = int(request.POST.get('n2', ''))
        op = request.POST.get('op', '')

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

        actionRecord = f"User Performed {op}."
        userAction = UserAction.objects.create(user = request.user, action = actionRecord)
        return render(request, 'calculator/result.html', {'result': result})

    return render(request, 'calculator/calculate.html')
