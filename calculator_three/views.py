from django.shortcuts import render

from calculator_three.models import CalculatorHistory


def index_page(request):
    context = {"page_name": "Калькулятор"}

    if request.method == "POST":
        number_one = int(request.POST["number_one"])
        number_two = int(request.POST["number_two"])

        answer = number_one + number_two

        CalculatorHistory(
            number_one=number_one, number_two=number_two, answer=answer
        ).save()
    elif request.method == "GET":
        user_choose = request.GET.get("select_data")
        if user_choose == "select_all":
            context["data"] = CalculatorHistory.objects.all()
        elif user_choose == "select_positive":
            context["data"] = CalculatorHistory.objects.filter(answer__gt=0)
        elif user_choose == "select_negative":
            context["data"] = CalculatorHistory.objects.filter(answer__lt=0)
        elif user_choose == "select_list":
            context["data"] = CalculatorHistory.objects.filter(answer__in=[30, 40, 57])

    return render(request, "calculator_three/index_page.html", context)
