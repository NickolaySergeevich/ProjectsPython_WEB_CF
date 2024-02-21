from django.shortcuts import render

from calculator_two.models import CalculatorHistory


def index_page(request):
    context = {"page_name": "Калькулятор"}

    if request.method == "POST":
        number_one = int(request.POST["number_one"])
        number_two = int(request.POST["number_two"])

        answer = number_one + number_two

        CalculatorHistory(
            number_one=number_one, number_two=number_two, answer=answer
        ).save()

    context["data"] = CalculatorHistory.objects.all()

    return render(request, "calculator_two/index_page.html", context)
